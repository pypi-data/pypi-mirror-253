import unittest
import uuid
from decimal import Decimal
from unittest.mock import Mock, patch, MagicMock
from skipcash.api_resources import Payment
from skipcash.client import SkipCash
from skipcash.responses import PaymentResponse
from skipcash.schema import PaymentInfo
from skipcash.exceptions import PaymentInfoError, PaymentResponseError, PaymentValidationError


class TestPaymentCreation(unittest.TestCase):
    """
    TestPaymentCreation Unit Test
    """
    def setUp(self):
        self.client = SkipCash('client_id', 'key_id', 'key_secret', 'webhook_secret', use_sandbox=True)
        self.payment = Payment(self.client)

    @patch('skipcash.utils.HttpClient.post')
    def test_create_payment_success(self, mock_post):
        obj_id = str(uuid.uuid4())

        mock_response_data = {
            'resultObj': {
                'id': obj_id,
                'statusId': 0,
                'created': '2024-01-28T19:07:22Z',
                'payUrl': 'https://codelounge.io/pay/b05ade9c-0d23-49f9-9469-928889521c93',
                'amount': '100.00',
                'currency': 'QAR',
                'transactionId': '00030203',
                'visaId': None,
                'refundId': None,
                'refundStatusId': None,
                'tokenId': None,
                'status': 'new',
                'cardType': 0
            },
            'returnCode': 200,
            'errorCode': None,
            'errorMessage': None,
            'hasError': False,
            'hasValidationError': False
        }
        # Configure the mock object
        mock_post.return_value.json.return_value = mock_response_data
        mock_post.return_value.status_code = 200

        payment_info = PaymentInfo(
            key_id=str(uuid.uuid4()),
            amount=Decimal('100.00'),
            first_name='John',
            last_name='Doe',
            phone='+97400000001',
            email='john.doe@example.com',
            street='123 Main St',
            city='Doha',
            state='QA',
            country='QA',
            postal_code='00000',
            transaction_id='00030203',
            custom_fields={
                'Custom1': 'value1',
                'Custom2': 'value2',
                'Custom3': 'value3',
                'Custom4': 'value4',
                'Custom5': 'value5',
                'Custom6': 'value6',
                'Custom7': 'value7',
                'Custom8': 'value8',
                'Custom9': 'value9',
                'Custom10': 'value10',
            }
        )

        # Execute the method under test
        result = self.payment.create_payment(payment_info)

        # Verify the results
        self.assertIsNotNone(result)
        self.assertIsInstance(result, PaymentResponse)
        self.assertEqual(result.id, obj_id)

    @patch('skipcash.utils.HttpClient.post')
    def test_create_payment_failure_invalid_info(self, mock_post):
        obj_id = str(uuid.uuid4())

        mock_response_data = {
            'resultObj': {
                'id': obj_id,
                'statusId': 0,
                'created': '2024-01-28T19:07:22Z',
                'payUrl': 'https://codelounge.io/pay/b05ade9c-0d23-49f9-9469-928889521c93',
                'amount': '100.00',
                'currency': 'QAR',
                'transactionId': '00030203',
                'visaId': None,
                'refundId': None,
                'refundStatusId': None,
                'tokenId': None,
                'status': 'new',
                'cardType': 0
            },
            'returnCode': 200,
            'errorCode': None,
            'errorMessage': None,
            'hasError': False,
            'hasValidationError': False
        }
        # Configure the mock object
        mock_post.return_value.json.return_value = mock_response_data
        mock_post.return_value.status_code = 200

        payment_info = PaymentInfo(
            key_id=str(uuid.uuid4()),
            amount=Decimal('100.00'),
            first_name='John',
            last_name='Doe',
            phone='+97400000001',
            email='john.doe@example.com',
            street='123 Main St',
            city='Doha',
            state='QA',
            country='QA',
            postal_code='00000',
            transaction_id='00030203',
            custom_fields={
                'Custom1': 'value1',
                'Custom2': 'value2',
                'Custom3': 'value3',
                'Custom4': 'value4',
                'Custom5': 'value5',
                'Custom6': 'value6',
                'Custom7': 'value7',
                'Custom8': 'value8',
                'Custom9': 'value9',
                'Custom10': 'value10',
                'Custom11': 'value11',
            }
        )

        # Assertions
        with self.assertRaises(PaymentInfoError):
            self.payment.create_payment(payment_info)

    @patch('skipcash.utils.HttpClient.post')
    def test_create_payment_failure_api_signature_error(self, mock_post):
        # Setup
        mock_response_data = {
            'returnCode': 400,
            'errorCode': 0,
            'errorMessage': 'Signature does not match!',
            'error': None,
            'validationErrors': [{'propertyName': '', 'errorMessage': 'Signature does not match!'}],
            'hasError': False,
            'hasValidationError': True
        }
        # Configure the mock object
        mock_post.return_value.json.return_value = mock_response_data
        mock_post.return_value.status_code = 400

        payment_info = PaymentInfo(
            key_id=str(uuid.uuid4()),
            amount=Decimal('100.00'),
            first_name='John',
            last_name='Doe',
            phone='+97400000001',
            email='john.doe@example.com',
            street='123 Main St',
            city='Doha',
            state='QA',
            country='QA',
            postal_code='00000',
            transaction_id='00030203',
            custom_fields={
                'Custom1': 'value1',
                'Custom2': 'value2',
                'Custom3': 'value3',
                'Custom4': 'value4',
                'Custom5': 'value5',
                'Custom6': 'value6',
                'Custom7': 'value7',
                'Custom8': 'value8',
                'Custom9': 'value9',
                'Custom10': 'value10',
            }
        )
        # Assertions
        with self.assertRaises(PaymentValidationError):
            self.payment.create_payment(payment_info)

    @patch('skipcash.utils.HttpClient.post')
    def test_create_payment_failure_api_invalid_data_error(self, mock_post):
        # Setup
        mock_response_data = {
            'returnCode': 200,
            'errorCode': None,
            'errorMessage': None,
            'hasError': False,
            'hasValidationError': False
        }
        # Configure the mock object
        mock_post.return_value.json.return_value = mock_response_data
        mock_post.return_value.status_code = 200

        payment_info = PaymentInfo(
            key_id=str(uuid.uuid4()),
            amount=Decimal('100.00'),
            first_name='John',
            last_name='Doe',
            phone='+97400000001',
            email='john.doe@example.com',
            street='123 Main St',
            city='Doha',
            state='QA',
            country='QA',
            postal_code='00000',
            transaction_id='00030203',
            custom_fields={
                'Custom1': 'value1',
                'Custom2': 'value2',
                'Custom3': 'value3',
                'Custom4': 'value4',
                'Custom5': 'value5',
                'Custom6': 'value6',
                'Custom7': 'value7',
                'Custom8': 'value8',
                'Custom9': 'value9',
                'Custom10': 'value10',
            }
        )
        # Assertions
        with self.assertRaises(PaymentResponseError):
            self.payment.create_payment(payment_info)


if __name__ == '__main__':
    unittest.main()

