from skipcash.api_operations import create, retrieve
from skipcash.client import SkipCash
from skipcash.responses import PaymentResponseHandler, PaymentResponse
from skipcash.schema import PaymentInfo
from skipcash.exceptions import PaymentResponseError, PaymentValidationError, PaymentInfoError, PaymentRetrievalError
from skipcash.utils import is_valid_uuid


class Payment:
    """Class representing a payment.

    Args:
        client (SkipCash): The SkipCash client used to make API requests.

    """
    def __init__(self, client: SkipCash):
        self.client = client

    def create_payment(self, payment_info: PaymentInfo):
        """
        :param payment_info: The payment information provided as a PaymentInfo object.
        :return: An instance of the PaymentResponse class representing the payment details.

        This method creates a payment using the provided payment_info. It first validates the payment_info object using the validate() method of the PaymentInfo class. If the validation fails
        *, a PaymentInfoError is raised.

        Next, the payment_info object is converted to a dictionary using the to_skipcash_dict() method of the PaymentInfo class. This dictionary is then sent as a JSON payload to the create
        *() function with a POST request to the "/api/v1/payments" endpoint.

        The response received from the create() function is parsed as JSON and stored in the response_data variable. The response_data is then passed to the PaymentResponseHandler class to process
        * the response. If the response processing is successful, the payment response is returned as a PaymentResponse object.

        If any error occurs during the response processing, such as a PaymentResponseError or PaymentValidationError, it is raised and propagated to the caller.
        """
        try:
            payment_info.validate()
        except PaymentInfoError as e:
            raise e
        data = payment_info.to_skipcash_dict()
        response = create(self.client, "/api/v1/payments", data)
        response_data = response.json()
        response_handler = PaymentResponseHandler(response_data)
        try:
            payment_response: PaymentResponse = response_handler.process_response()
            return payment_response
        except (PaymentResponseError, PaymentValidationError) as e:
            raise e

    def get_payment(self, payment_id):
        """
        :param payment_id: A string representing the ID of the payment to retrieve.
        :return: An instance of the PaymentResponse class representing the payment details.

        Raises:
            PaymentRetrievalError: If the provided payment_id is empty or not a valid UUID.
            PaymentResponseError: If there is an error processing the payment response.
            PaymentValidationError: If there is a validation error in the payment response.

        """
        if not payment_id or not is_valid_uuid(payment_id):
            raise PaymentRetrievalError("Please provide a valid payment_id")
        response = retrieve(self.client, "/api/v1/payments/{}".format(payment_id))
        response_data = response.json()
        response_handler = PaymentResponseHandler(response_data)
        try:
            payment_response: PaymentResponse = response_handler.process_response()
            return payment_response
        except (PaymentResponseError, PaymentValidationError) as e:
            raise e
