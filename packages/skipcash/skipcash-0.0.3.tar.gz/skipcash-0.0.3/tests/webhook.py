import unittest
from unittest.mock import Mock, patch

from skipcash.api_resources import Webhook, Payment
from skipcash.client import SkipCash
from skipcash.exceptions import WebhookValidationError, WebhookSignatureError, PaymentRetrievalError
from skipcash.responses import PaymentResponse


class TestWebhook(unittest.TestCase):
    """
    This class provides unit tests for the TestWebhook class.
    """

    def setUp(self):
        self.client = SkipCash('client_id', 'key_id', 'key_secret', 'webhook_secret', use_sandbox=True)
        self.webhook = Webhook(self.client)

    @patch('skipcash.utils.validate_signature')
    @patch.object(Payment, 'get_payment')
    def test_webhook_validate_success(self, mock_get_payment, mock_validate_signature):
        # Configure the mock for validate_signature
        mock_validate_signature.return_value = True

        # Configure the mock for get_payment
        mock_payment_response = PaymentResponse(
            id='32943d5e-3fd9-4794-8a89-b1200ebcf0f7',
            status_id=2,
            created='2024-01-28T19:07:22Z',
            pay_url='https://codelounge.io/pay/b05ade9c-0d23-49f9-9469-928889521c93',
            amount='100.00',
            currency='QAR',
            transaction_id='00030203',
            visa_id='7064596254436292404008',
            status='SUCCESS',
            refund_id=None,
            refund_status_id=None,
            token_id='',
            card_type=1
        )
        mock_get_payment.return_value = mock_payment_response

        # Mock payload and signature (these would normally come from SkipCash server)
        payload = {
            'PaymentId': '32943d5e-3fd9-4794-8a89-b1200ebcf0f7',
            'Amount': '100.00',
            'StatusId': 2,
            'TransactionId': '00030203',
            'Custom1': None,
            'Custom2': None,
            'Custom3': None,
            'Custom4': None,
            'Custom5': None,
            'Custom6': None,
            'Custom7': None,
            'Custom8': None,
            'Custom9': None,
            'Custom10': None,
            'VisaId': '7064596254436292404008',
            'TokenId': '',
            'CardType': 1
        }
        signature = 'SjH/NKsp6wPUKd5uAufnRhmPz+MT7i6bGGC5dtTAcco='

        # Execute the method under test
        self.webhook.validate(payload, signature)
        self.assertEqual(self.webhook.payment, mock_payment_response)

    @patch('skipcash.utils.validate_signature')
    @patch.object(Payment, 'get_payment')
    def test_webhook_validate_failure(self, mock_get_payment, mock_validate_signature):
        # Configure the mock for validate_signature
        mock_validate_signature.return_value = False

        # Configure the mock for get_payment
        mock_payment_response = PaymentResponse(
            id='32943d5e-3fd9-4794-8a89-b1200ebcf0f7',
            status_id=2,
            created='2024-01-28T19:07:22Z',
            pay_url='https://codelounge.io/pay/b05ade9c-0d23-49f9-9469-928889521c93',
            amount='100.00',
            currency='QAR',
            transaction_id='00030203',
            visa_id='7064596254436292404008',
            status='SUCCESS',
            refund_id=None,
            refund_status_id=None,
            token_id='',
            card_type=1
        )
        mock_get_payment.return_value = mock_payment_response

        # Mock payload and signature (these would normally come from SkipCash server)
        payload = {
            'PaymentId': '32943d5e-3fd9-4794-8a89-b1200ebcf0f7',
            'Amount': '100.00',
            'StatusId': 2,
            'TransactionId': '00030203',
            'Custom1': None,
            'Custom2': None,
            'Custom3': None,
            'Custom4': None,
            'Custom5': None,
            'Custom6': None,
            'Custom7': None,
            'Custom8': None,
            'Custom9': None,
            'Custom10': None,
            'VisaId': '7064596254436292404008',
            'TokenId': '',
            'CardType': 1
        }
        signature = 'IxElhp2gTc50SmHHEFTOoJ44cQjFYJzBExNDHJjbmzY='

        # Execute the method under test
        with self.assertRaises(WebhookSignatureError):
            self.webhook.validate(payload, signature)

    @patch('skipcash.utils.validate_signature')
    @patch.object(Payment, 'get_payment')
    def test_webhook_validate_failure_invalid_payload(self, mock_get_payment, mock_validate_signature):
        # Configure the mock for validate_signature
        mock_validate_signature.return_value = False

        # Configure the mock for get_payment
        mock_payment_response = PaymentResponse(
            id='32943d5e-3fd9-4794-8a89-b1200ebcf0f7',
            status_id=2,
            created='2024-01-28T19:07:22Z',
            pay_url='https://codelounge.io/pay/b05ade9c-0d23-49f9-9469-928889521c93',
            amount='100.00',
            currency='QAR',
            transaction_id='00030203',
            visa_id='7064596254436292404008',
            status='SUCCESS',
            refund_id=None,
            refund_status_id=None,
            token_id='',
            card_type=1
        )
        mock_get_payment.return_value = mock_payment_response

        # Mock payload and signature (these would normally come from SkipCash server)
        payload = {
            'PaymentId': '',
            'Amount': '100.00',
            'StatusId': 2,
            'TransactionId': '00030203',
            'Custom1': None,
            'Custom2': None,
            'Custom3': None,
            'Custom4': None,
            'Custom5': None,
            'Custom6': None,
            'Custom7': None,
            'Custom8': None,
            'Custom9': None,
            'Custom10': None,
            'VisaId': '7064596254436292404008',
            'TokenId': '',
            'CardType': 1
        }
        signature = 'EuBLCxVU7hJHiHeYWWY2TYvWrVAUsEqn1MRGsLND8uI='

        # Execute the method under test
        with self.assertRaises(WebhookValidationError):
            self.webhook.validate(payload, signature)

    @patch('skipcash.utils.validate_signature')
    @patch.object(Payment, 'get_payment')
    def test_webhook_validate_payment_not_found(self, mock_get_payment, mock_validate_signature):
        # Mock validate_signature to return True (signature is valid)
        mock_validate_signature.return_value = True

        # Configure mock_get_payment to raise PaymentRetrievalError when called
        mock_get_payment.side_effect = PaymentRetrievalError("Payment not found")

        # Mock payload and signature (these would normally come from SkipCash server)
        payload = {
            'PaymentId': '32943d5e-3fd9-4794-8a89-b1200ebcf0f7',
            'Amount': '100.00',
            'StatusId': 2,
            'TransactionId': '00030203',
            'Custom1': None,
            'Custom2': None,
            'Custom3': None,
            'Custom4': None,
            'Custom5': None,
            'Custom6': None,
            'Custom7': None,
            'Custom8': None,
            'Custom9': None,
            'Custom10': None,
            'VisaId': '7064596254436292404008',
            'TokenId': '',
            'CardType': 1
        }
        signature = 'SjH/NKsp6wPUKd5uAufnRhmPz+MT7i6bGGC5dtTAcco='

        # Execute the method under test and expect it to raise a WebhookValidationError
        with self.assertRaises(WebhookValidationError) as context:
            self.webhook.validate(payload, signature)

        # Optionally, assert that the exception message contains expected content
        self.assertIn("Payment not found", str(context.exception))


if __name__ == '__main__':
    unittest.main()
