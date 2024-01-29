from typing import Union

from skipcash.client import SkipCash
from skipcash.exceptions import WebhookValidationError, PaymentResponseError, PaymentValidationError, PaymentRetrievalError, WebhookSignatureError
from skipcash.schema import WebhookEvent
from .payment import Payment
from skipcash.utils import validate_signature, validation_required
from skipcash.responses import PaymentResponse


class Webhook:
    """
    The `Webhook` class represents a webhook for receiving payment events from SkipCash. It provides methods for validating the webhook payload and processing the event data.

    Attributes:
        - `client`: An instance of `SkipCash` representing the SkipCash API client.
        - `_is_validated`: A boolean indicating whether the webhook payload has been successfully validated.
        - `payment`: An instance of `PaymentResponse` representing the payment associated with the webhook.

    Methods:
        - `__init__(self, client: SkipCash)`: Initializes a new instance of the `Webhook` class.

        - `validate(self, payload, signature)`: Validates the webhook payload and raises an error if it is invalid.

        - `process_event(self, data)`: Processes the event data received from the webhook.

    """
    def __init__(self, client: SkipCash):
        self.client = client
        self._is_validated = False
        self.payment: Union[None, PaymentResponse] = None

    def validate(self, payload, signature):
        """Validates a webhook payload and signature.

        :param payload: The payload of the webhook.
        :param signature: The signature of the webhook payload.
        :return: None
        :raises WebhookSignatureError: If the signature is invalid.
        :raises WebhookValidationError: If the payload is missing PaymentId or is not valid.
        """
        self._is_validated = True
        is_valid = validate_signature(payload, signature, self.client.webhook_secret)
        if not is_valid:
            raise WebhookSignatureError("Invalid signature for webhook")
        if 'PaymentId' not in payload or not payload['PaymentId']:
            raise WebhookValidationError("Payload is missing PaymentId")
        payment = Payment(self.client)
        try:
            payment_detail: PaymentResponse = payment.get_payment(payload['PaymentId'])
            self.payment = payment_detail
        except (PaymentRetrievalError, PaymentResponseError, PaymentValidationError) as e:
            raise WebhookValidationError("Provided payload is not valid skip cash payment transaction, original exception was: {}".format(e))

    @validation_required
    def process_event(self, data):
        """
        Process an event.

        :param data: The data for the event.
        :type data: Any
        :return: The processed event.
        :rtype: WebhookEvent
        """
        event = WebhookEvent(data)
        return event
