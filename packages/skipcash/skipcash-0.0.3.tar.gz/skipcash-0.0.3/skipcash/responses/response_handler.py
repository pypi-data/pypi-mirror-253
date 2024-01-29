from skipcash.exceptions import PaymentResponseError, PaymentValidationError
from skipcash.responses import PaymentResponse


class PaymentResponseHandler:
    """
    PaymentResponseHandler is a class that handles the response from a payment API. It processes the response and returns the corresponding PaymentResponse object.

    Methods:
        - __init__(self, response): Initializes the PaymentResponseHandler object with the response from the payment API.
        - process_response(): Processes the response and returns a PaymentResponse object.

    Attributes:
        - response: The response from the payment API.

    Exceptions:
        - PaymentResponseError: Raised when there is a general error in the payment response.
        - PaymentValidationError: Raised when there are validation errors in the payment response.

    Example Usage:

    response = {...}  # Response received from the payment API
    handler = PaymentResponseHandler(response)
    payment_response = handler.process_response()
    """
    def __init__(self, response):
        self.response = response

    def process_response(self):
        """
        Process the response from the payment API.

        :return: The processed payment response.
        :raises PaymentResponseError: If a general payment error occurred.
        :raises PaymentValidationError: If a validation error occurred.
        :raises PaymentResponseError: If no result object is found in the response.
        """
        if self.response.get('hasError', False):
            # Handle general error
            error_message = self.response.get('errorMessage', 'Unknown error')
            error_code = self.response.get('errorCode', 'Unknown code')
            raise PaymentResponseError(error_message, error_code)

        if self.response.get('hasValidationError', False):
            # Handle validation error
            validation_errors = self.response.get('validationErrors', [])
            error_details = [(err.get('propertyName', 'Unknown property'), err.get('errorMessage', 'Unknown validation error')) for err in validation_errors]
            if error_details:
                raise PaymentValidationError(error_details)

        # If there are no errors, parse the successful response
        result_obj = self.response.get('resultObj')
        if result_obj is not None:
            payment_response = PaymentResponse.from_json(result_obj)
            return payment_response

        # Handle unexpected case: successful return code but no resultObj
        raise PaymentResponseError("No result object found in response", self.response.get('returnCode'))
