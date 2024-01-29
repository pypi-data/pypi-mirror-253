from decimal import Decimal

from skipcash.exceptions import WebhookValidationError
from skipcash.utils import is_decimal_with_max_two_places


class WebhookEvent:
    """

    The `WebhookEvent` class represents a webhook event received from an external payment system.

    Attributes:
        payment_id (str): The ID of the payment associated with the event.
        amount (Decimal): The amount of the payment.
        status_id (int): The ID indicating the status of the payment.
        status (str): The status of the payment. Possible values are "SUCCESS" and "FAILED_OR_CANCELLED".
        transaction_id (str): The ID of the transaction related to the payment.
        visa_id (str): The ID of the Visa card used for the payment.
        token_id (str): The ID of the payment token associated with the payment.
        card_type (str): The type of the card used for the payment.
        custom_fields (dict): A dictionary of custom fields associated with the event.

    Methods:
        validate_data(data): Validates the data received in the webhook event.

    Exceptions:
        WebhookValidationError: Raised when invalid data is received in the webhook event.

    Example usage:
        data = {
            'PaymentId': '1234',
            'Amount': '10.00',
            'StatusId': 2,
            'TransactionId': '5678',
            'VisaId': '9876',
            'TokenId': 'abcd',
            'CardType': 'VISA',
            'Custom1': 'Value1',
            'Custom2': 'Value2'
        }

        event = WebhookEvent(data)

    Note:
        This class assumes that the data passed in the constructor is a valid webhook event payload as per the expected format.
    """
    def __init__(self, data):
        self.validate_data(data)
        self.payment_id = data.pop('PaymentId')
        self.amount = Decimal(data.pop('Amount'))
        self.status_id = data.pop('StatusId')
        self.status = "SUCCESS" if self.status_id == 2 else "FAILED_OR_CANCELLED"
        self.transaction_id = data.pop('TransactionId')
        self.visa_id = data.pop('VisaId')
        self.token_id = data.pop('TokenId')
        self.card_type = data.pop('CardType')
        self.custom_fields = {}
        # if other custom fields are there.
        if len(data) > 0:
            for field in data:
                self.custom_fields[field] = data.get(field)

    @staticmethod
    def validate_data(data):
        """
        :param data: A dictionary containing the data to be validated.
        :return: None

        This method validates the data dictionary against a set of valid fields. If any invalid field is found or if the 'Amount' field is not a valid decimal number with a maximum of two decimal
        * places, a WebhookValidationError is raised.

        Valid fields include: 'PaymentId', 'Amount', 'StatusId', 'TransactionId', 'Custom1', 'Custom2', 'Custom3', 'Custom4', 'Custom5', 'Custom6', 'Custom7', 'Custom8', 'Custom9', 'Custom10
        *', 'VisaId', 'TokenId', 'CardType'.

        Example usage:

        ```
        data = {
            "PaymentId": "12345",
            "Amount": "10.50",
            "StatusId": "1",
            "TransactionId": "67890",
            "Custom1": "Value1",
            "Custom2": "Value2",
            "Custom3": "Value3",
            "Custom4": "Value4",
            "Custom5": "Value5",
            "Custom6": "Value6",
            "Custom7": "Value7",
            "Custom8": "Value8",
            "Custom9": "Value9",
            "Custom10": "Value10",
            "VisaId": "V12345",
            "TokenId": "T67890",
            "CardType": "VISA"
        }

        try:
            validate_data(data)
            print("Data is valid")
        except WebhookValidationError as e:
            print(f"Validation error: {str(e)}")
        ```
        """
        valid_fields = [
            "PaymentId",
            "Amount",
            "StatusId",
            "TransactionId",
            "Custom1",
            "Custom2",
            "Custom3",
            "Custom4",
            "Custom5",
            "Custom6",
            "Custom7",
            "Custom8",
            "Custom9",
            "Custom10",
            "VisaId",
            "TokenId",
            "CardType"
        ]
        for field in valid_fields:
            if field not in data:
                raise WebhookValidationError(f"Invalid field {field}")

        if not is_decimal_with_max_two_places(data.get("Amount")):
            raise WebhookValidationError(f"Amount {data.get('Amount')} not a valid decimal number")
