import logging
from collections import OrderedDict
from django import forms
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.template.response import TemplateResponse
from django.utils.crypto import get_random_string
from django.utils.safestring import SafeString
from django.utils.translation import gettext_lazy as _
from pretix.base.forms import SecretKeySettingsField
from pretix.base.middleware import _render_csp, get_language_from_request
from pretix.base.models import OrderPayment, OrderRefund
from pretix.base.payment import BasePaymentProvider, PaymentException
from pretix.multidomain.urlreverse import build_absolute_uri, eventreverse
from pretix.plugins.stripe.forms import StripeKeyValidator

from pretix_sumup import sumup_client

logger = logging.getLogger("pretix.plugins.sumup")


class SumUp(BasePaymentProvider):
    identifier = "sumup"
    verbose_name = _("Credit card via SumUp")
    public_name = _("Credit card")
    abort_pending_allowed = True

    @property
    def settings_form_fields(self):
        d = OrderedDict(
            [
                (
                    "access_token",
                    SecretKeySettingsField(
                        label=_("API Key"),
                        required=True,
                        help_text=_(
                            "API keys are authorization tokens that allow pretix to call SumUp on your behalf. "
                            '<a href="https://developer.sumup.com/api-keys" target="_blank">Click here to '
                            "manage API Keys in SumUp</a>"
                        ),
                        validators=(StripeKeyValidator("sup_sk_"),),
                    ),
                ),
                (
                    "merchant_code",
                    forms.CharField(
                        widget=forms.TextInput(
                            attrs={
                                "maxlength": 10,
                                "readonly": "readonly",
                                "placeholder": _("Automatically filled in"),
                            }
                        ),
                        label=_("Merchant Code"),
                    ),
                ),
            ]
            + list(super().settings_form_fields.items())
        )

        d.move_to_end("_enabled", last=False)
        return d

    def settings_form_clean(self, cleaned_data):
        cleaned_data = super().settings_form_clean(cleaned_data)
        access_token = cleaned_data.get("payment_sumup_access_token")
        if access_token is None:
            # access token was already validated and turned out to be invalid
            return cleaned_data
        merchant_code = sumup_client.validate_access_token_and_get_merchant_code(
            access_token
        )
        cleaned_data["payment_sumup_merchant_code"] = merchant_code
        return cleaned_data

    def is_allowed(self, request, total=None):
        if total is None:
            return True
        # minimum amount is 1 EUR or similar in other currencies
        return total >= 1

    def execute_payment(self, request, payment):
        payment_id = payment.local_id
        order = payment.order
        event = order.event

        has_valid_checkout = self._synchronize_payment_status(payment)
        if has_valid_checkout:
            return
        try:
            checkout_id = sumup_client.create_checkout(
                checkout_reference=f"{event.slug}/{order.code}/{payment_id}",
                amount=payment.amount,
                currency=event.currency,
                description=f"{event.name} #{order.code}",
                merchant_code=self.settings.get("merchant_code"),
                return_url=build_absolute_uri(
                    event,
                    "plugins:pretix_sumup:checkout_event",
                    kwargs={"payment": payment.pk},
                ),
                access_token=self.settings.get("access_token"),
            )

            info_data = payment.info_data
            info_data["sumup_checkout_id"] = checkout_id
            payment.info_data = info_data
            payment.save()
        except Exception as err:
            payment.fail(info={"error": str(err)})
            logger.exception(f"Error while creating sumup checkout: {err}")
            raise PaymentException(_("Error while creating sumup checkout"))

    def checkout_confirm_render(self, request, **kwargs):
        return _(
            "After confirmation you will be redirected to SumUp to complete the payment."
        )

    def payment_form_render(self, request, **kwargs):
        return self.checkout_confirm_render(request, **kwargs)

    def payment_pending_render(self, request, payment):
        checkout_id = payment.info_data["sumup_checkout_id"]
        if checkout_id is None:
            return ""

        # Synchronize the payment status as backup if the return webhook fails
        self._synchronize_payment_status(payment)

        return SafeString(
            '<iframe src="{}" width="100%" height="630" frameBorder=0>'.format(
                eventreverse(
                    payment.order.event,
                    "plugins:pretix_sumup:payment_widget",
                    kwargs={
                        "payment": payment.pk,
                        "order": payment.order.code,
                        "secret": payment.order.secret,
                    },
                )
            )
        )

    def payment_is_valid_session(self, request):
        return True

    def cancel_payment(self, payment):
        checkout_id = payment.info_data.get("sumup_checkout_id")
        if checkout_id:
            try:
                sumup_client.cancel_checkout(
                    checkout_id, self.settings.get("access_token")
                )
            except Exception as err:
                logger.warn(f"Error while canceling sumup checkout: {err}")
                pass  # Ignore errors, this hasn't any impact on us
        super().cancel_payment(payment)

    def payment_refund_supported(self, payment):
        self._synchronize_payment_status(payment)
        return payment.info_data.get("sumup_transaction") is not None

    def payment_partial_refund_supported(self, payment):
        self._synchronize_payment_status(payment)
        return payment.info_data.get("sumup_transaction") is not None

    def execute_refund(self, refund):
        payment = refund.payment
        transaction = payment.info_data.get("sumup_transaction")
        if not transaction:
            logger.exception(
                "Error while refunding sumup transaction. No transaction found"
            )
            raise PaymentException(_("Error while refunding sumup transaction"))
        try:
            sumup_client.refund_transaction(
                transaction_id=transaction["id"],
                amount=float(refund.amount),
                access_token=self.settings.get("access_token"),
            )
            refund.done()
        except Exception as err:
            logger.exception(f"Error while refunding sumup transaction: {err}")
            refund.state = OrderRefund.REFUND_STATE_FAILED
            refund.save(update_fields=["state"])
            raise PaymentException(_("Error while refunding sumup transaction"))

        # Synchronize the transaction to get the refund status
        self._try_synchronize_transaction(payment, transaction["id"])

    def render_invoice_text(self, order, payment):
        transaction = payment.info_data.get("sumup_transaction")
        if not transaction:
            return ""
        return _("Payed via SumUp\n{} **** **** **** {}\nAuth code: {}").format(
            transaction["card"]["type"],
            transaction["card"]["last_4_digits"],
            transaction["auth_code"],
        )

    def payment_presale_render(self, payment):
        transaction = payment.info_data.get("sumup_transaction")
        if not transaction:
            return ""

        return get_template("pretix_sumup/payment_admin_info.html").render(
            {
                "card_type": transaction["card"]["type"],
                "card_last_4_digit": transaction["card"]["last_4_digits"],
                "transaction_code": transaction["transaction_code"],
                "merchant_code": transaction["merchant_code"],
            }
        )

    def payment_control_render(self, order, payment):
        return self.payment_presale_render(payment)

    def matching_id(self, payment):
        transaction = payment.info_data.get("sumup_transaction")
        if not transaction:
            return None
        return transaction.get("transaction_code")

    def api_payment_details(self, payment):
        return {"sumup_transaction": payment.info_data.get("sumup_transaction")}

    def _synchronize_payment_status(self, payment, force=False):
        """
        Synchronizes the payment status with the SumUp Checkout.
        :param force: True if the payment status should be synchronized even if it is already confirmed
        :param payment: The OrderPayment object to synchronize
        :return: True if a SumUp checkout exists which hasn't failed, False if no checkout exists or the checkout has failed
        """
        checkout_id = payment.info_data.get("sumup_checkout_id")
        if not checkout_id:
            return False
        if not force:
            if (
                payment.state == OrderPayment.PAYMENT_STATE_CONFIRMED
                and payment.info_data.get("sumup_transaction") is not None
            ):
                return True
        try:
            checkout = sumup_client.get_checkout(
                checkout_id, self.settings.get("access_token")
            )
        except Exception as err:
            logger.exception(f"Error while synchronizing sumup checkout: {err}")
            raise PaymentException(_("Error while synchronizing sumup checkout"))
        if checkout["status"] == "PAID":
            # Every try of processing the payment results in a transaction, we only care about the successful one
            transaction_id = next(
                (
                    transaction.get("id")
                    for transaction in checkout["transactions"]
                    if transaction["status"] == "SUCCESSFUL"
                ),
                None,
            )
            if transaction_id is not None:
                self._try_synchronize_transaction(payment, transaction_id)

            if not payment.state == OrderPayment.PAYMENT_STATE_CONFIRMED:
                payment.confirm()
            return True
        elif checkout["status"] == "PENDING":
            if not payment.state == OrderPayment.PAYMENT_STATE_PENDING:
                payment.state = OrderPayment.PAYMENT_STATE_PENDING
                payment.save(update_fields=["state"])
            return True
        elif checkout["status"] == "FAILED":
            if not payment.state == OrderPayment.PAYMENT_STATE_FAILED:
                payment.fail()
            return False

    def _try_synchronize_transaction(self, payment, transaction_id):
        try:
            transaction = sumup_client.get_transaction(
                transaction_id=transaction_id,
                access_token=self.settings.get("access_token"),
            )
            # split into multiple line is required to invoke the setter of info_data
            info_data = payment.info_data
            info_data["sumup_transaction"] = transaction
            payment.info_data = info_data
            payment.save()
        except Exception as err:
            logger.warn(f"Error while synchronizing sumup transaction: {err}")


def checkout_event(request, *args, **kwargs):
    provider = SumUp(request.event)
    order_payment = get_object_or_404(
        OrderPayment, pk=kwargs.get("payment"), order__event=request.event
    )
    provider._synchronize_payment_status(order_payment)
    return HttpResponse(status=204, content=b"")


def payment_widget(request, *args, **kwargs):
    provider = SumUp(request.event)
    order_payment = get_object_or_404(
        OrderPayment,
        pk=kwargs.get("payment"),
        order__event=request.event,
        order__code=kwargs.get("order"),
        order__secret=kwargs.get("secret"),
    )
    # Synchronize the payment status as backup if the return webhook fails
    provider._synchronize_payment_status(order_payment)
    checkout_id = order_payment.info_data.get("sumup_checkout_id")
    if not checkout_id:
        raise ValidationError(_("No SumUp checkout ID found."))

    csp_nonce = get_random_string(10)
    csp = {
        "default-src": ["*.sumup.com"],
        "script-src": [f"'nonce-{csp_nonce}'", "*.sumup.com"],
        "style-src": [
            f"'nonce-{csp_nonce}'",
            "*.sumup.com",
            "'unsafe-inline'",  # workaround as sumup don't pass the nonce to the lazy loaded input fields
        ],
        "frame-src": [
            "*"  # sumup may due to 3DS verification load a site from the bank of the customer
        ],
        "img-src": ["*.sumup.com"],
        "connect-src": ["*.sumup.com"],
        "frame-ancestors": ["'self'"],
    }
    csp_header = {"Content-Security-Policy": _render_csp(csp)}
    if (
        order_payment.state == OrderPayment.PAYMENT_STATE_PENDING
        or order_payment.state == OrderPayment.PAYMENT_STATE_FAILED
    ):
        context = {
            "checkout_id": checkout_id,
            "email": order_payment.order.email,
            "retry": order_payment.state == OrderPayment.PAYMENT_STATE_FAILED,
            "locale": _get_sumup_locale(request),
            "csp_nonce": csp_nonce,
        }
    elif order_payment.state == OrderPayment.PAYMENT_STATE_CONFIRMED:
        # The payment was paid in the meantime, reload the containing page to show the success message
        context = {"reload": True, "csp_nonce": csp_nonce}
    else:
        # Invalid state, nothing to see here
        return HttpResponse(status=404)
    return TemplateResponse(
        template="pretix_sumup/payment_widget.html",
        context=context,
        request=request,
        headers=csp_header,
    )


def _get_sumup_locale(request):
    language = get_language_from_request(request)
    if language == "de" or language == "de-informal":
        return "de-DE"
    elif language == "fr":
        return "fr-FR"
    return "en-GB"
