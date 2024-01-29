import unittest
import uuid
from unittest.mock import Mock, patch

from skipcash.api_resources import Payment
from skipcash.client import SkipCash
from skipcash.exceptions import PaymentRetrievalError, PaymentResponseError


class TestPaymentRetrieval(unittest.TestCase):
    """
    This class contains unit tests for the PaymentRetrieval class.
    """
    def setUp(self):
        self.client = SkipCash('client_id', 'key_id', 'key_secret', 'webhook_secret', use_sandbox=True)
        self.payment = Payment(self.client)

    @patch('skipcash.utils.HttpClient.get')
    def test_get_payment_success(self, mock_retrieve):
        obj_id = str(uuid.uuid4())
        # Setup
        mock_retrieve.return_value.json.return_value = {
            'resultObj': {
                'id': obj_id,
                'statusId': 0,
                'created': '2024-01-28T19:59:36Z',
                'payUrl': f'https://codelounge.io/pay/{obj_id}',
                'amount': '100.00',
                'currency': 'QAR',
                'transactionId': '00030203',
                'custom1': 'value1',
                'custom2': 'value2',
                'custom3': 'value3',
                'custom4': 'value4',
                'custom5': 'value5',
                'custom6': 'value6',
                'custom7': 'value7',
                'custom8': 'value8',
                'custom9': 'value9',
                'custom10': 'value10',
                'visaId': None,
                'refundId': None,
                'refundStatusId': None,
                'tokenId': '',
                'status': 'new',
                'cardType': 0
            },
            'returnCode': 200,
            'errorCode': 0,
            'errorMessage': None,
            'error': None,
            'validationErrors': None,
            'hasError': False,
            'hasValidationError': False
        }
        # Execution
        result = self.payment.get_payment(obj_id)

        # Assertions
        self.assertIsNotNone(result)
        self.assertEqual(result.id, obj_id)

    @patch('skipcash.utils.HttpClient.get')
    def test_get_payment_failure_invalid_id(self, mock_retrieve):
        # Setup
        mock_retrieve.return_value.json.return_value = {
            'id': ["The value '46a3f3a22e18-4f53-937b-be7924c64944' is not valid."]
        }
        # here it looks like uuid but it's as its' missing a segment. :) valid is 46a3f3a2-2e18-4f53-937b-be7924c64944
        obj_id = "46a3f3a22e18-4f53-937b-be7924c64944"
        mock_retrieve.return_value.status_code = 404
        # Assertions
        with self.assertRaises(PaymentRetrievalError):
            self.payment.get_payment(obj_id)

    @patch('skipcash.utils.HttpClient.get')
    def test_get_payment_failure_payment_not_found(self, mock_retrieve):
        # Setup
        mock_retrieve.return_value.json.return_value = {
            'returnCode': 404,
            'errorCode': 0,
            'errorMessage': 'Payment not found!',
            'error': {'code': 1, 'message': 'Payment not found!', 'messageDetail': None},
            'validationErrors': [],
            'hasError': True,
            'hasValidationError': False
        }
        obj_id = str(uuid.uuid4())
        mock_retrieve.return_value.status_code = 404
        # Assertions
        with self.assertRaises(PaymentResponseError):
            self.payment.get_payment(obj_id)


if __name__ == '__main__':
    unittest.main()
