
class PaymentResponse:
    """
    Represents a payment response.

    :param id: The payment ID.
    :type id: str
    :param status_id: The status ID of the payment.
    :type status_id: int
    :param created: The creation timestamp of the payment.
    :type created: str
    :param pay_url: The URL for payment.
    :type pay_url: str
    :param amount: The amount of the payment.
    :type amount: str
    :param currency: The currency of the payment.
    :type currency: str
    :param transaction_id: The transaction ID of the payment.
    :type transaction_id: str
    :param visa_id: The visa ID of the payment.
    :type visa_id: str
    :param status: The status of the payment.
    :type status: str
    :param refund_id: The refund ID of the payment.
    :type refund_id: str|null
    :param refund_status_id: The refund status ID of the payment.
    :type refund_status_id: str|null
    :param token_id: The token ID of the payment.
    :type token_id: str
    :param card_type: The type of card used for the payment.
    :type card_type: int
    :param custom_fields: Additional custom fields to include in the payment response.
    :type custom_fields: dict
    """
    def __init__(self, id, status_id, created, pay_url, amount, currency, transaction_id, visa_id, status, refund_id, refund_status_id, token_id, card_type, **custom_fields):
        self.id = id
        self.status_id = status_id
        self.created = created
        self.pay_url = pay_url
        self.amount = amount
        self.currency = currency
        self.transaction_id = transaction_id
        self.visa_id = visa_id
        self.status = status
        self.refund_id = refund_id
        self.refund_status_id = refund_status_id
        self.token_id = token_id
        self.card_type = card_type
        self.custom_fields = {}
        # Directly assign custom fields without nesting them
        for field_name, field_value in custom_fields.items():
            self.custom_fields.update({str(field_name).capitalize(): field_value})

    @classmethod
    def from_json(cls, data):
        """
        Create an instance of the class from JSON data.

        :param data: The JSON data.
        :type data: dict
        :return: An instance of the class.
        :rtype: PaymentResponse
        """
        # Extract the known fields and use the rest as custom fields
        known_field_names = ['id', 'statusId', 'created', 'payUrl', 'amount', 'currency', 'transactionId', 'visaId', 'status', 'refundId', 'refundStatusId', 'tokenId', 'cardType']
        known_fields = {field: data.pop(field, None) for field in known_field_names}
        # Fix field names to match constructor arguments
        known_fields_fixed = {
            'id': known_fields['id'],
            'status_id': known_fields['statusId'],
            'created': known_fields['created'],
            'pay_url': known_fields['payUrl'],
            'amount': known_fields['amount'],
            'currency': known_fields['currency'],
            'transaction_id': known_fields['transactionId'],
            'visa_id': known_fields['visaId'],
            'status': known_fields['status'],
            'refund_id': known_fields['refundId'],
            'refund_status_id': known_fields['refundStatusId'],
            'token_id': known_fields['tokenId'],
            'card_type': known_fields['cardType'],
        }
        # Remaining data is treated as custom fields
        return cls(**known_fields_fixed, **data)
