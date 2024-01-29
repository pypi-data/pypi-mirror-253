class SkipCashSDKError(Exception):
    """Base exception for all SDK errors."""
    pass


class PaymentCreationError(SkipCashSDKError):
    """Exception raised for payment creation errors."""
    pass


class PaymentRetrievalError(SkipCashSDKError):
    """Exception raised for payment retrieval errors."""
    pass


class WebhookValidationError(SkipCashSDKError):
    """Exception raised for webhook validation errors."""
    pass


class PaymentInfoError(SkipCashSDKError):
    """Exception raised for webhook validation errors."""
    pass


class PaymentResponseError(SkipCashSDKError):
    """Exception raised for errors in the payment response."""
    def __init__(self, message, code):
        super().__init__(message)
        self.code = code


class PaymentValidationError(SkipCashSDKError):
    """Exception raised for validation errors in the payment response."""
    def __init__(self, errors):
        # errors is expected to be a list of tuples (property_name, error_message)
        error_messages = ["{}: {}".format(prop, msg) for prop, msg in errors]
        super().__init__("; ".join(error_messages))
        self.errors = errors


class WebhookSignatureError(SkipCashSDKError):
    pass

