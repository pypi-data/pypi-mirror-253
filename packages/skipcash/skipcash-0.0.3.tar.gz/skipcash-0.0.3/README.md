
# SkipCash SDK for Python

The SkipCash SDK for Python enables developers to easily integrate SkipCash payment services into their Python applications. This SDK provides a convenient way to create and manage payments, handle webhooks, and interact with the SkipCash API.

## Features

- Create payments with various customization options.
- Retrieve payment information using payment IDs.
- Validate and process webhook events securely.
- Handle various exceptions and errors gracefully.

## Getting Started

### Prerequisites

- Python 3.x
- An active SkipCash account with access to API credentials.

### Installation

Currently, this SDK is provided as a Python module. Include it in your project by copying the SDK files to your project directory.

### Configuration

To use the SDK, you'll need your SkipCash API credentials. Initialize the `SkipCash` client with your credentials:

```python
from skipcash.client import SkipCash

skipcash = SkipCash(
    client_id='<your_client_id>',
    key_id='<your_client_key_id>',
    key_secret='<your_client_secret_key>',
    webhook_secret='<your_webhook_secret_key>',
    use_sandbox=True  # Set to False when moving to production
)
```

## Usage

### Creating a Payment

To create a payment, you need to prepare `PaymentInfo` with the necessary details:

```python
from decimal import Decimal
from skipcash.api_resources import Payment
from skipcash.schema import PaymentInfo
from skipcash.exceptions import PaymentResponseError, PaymentValidationError, PaymentInfoError
from skipcash.client import SkipCash

skipcash = SkipCash(
    client_id='<your_client_id>',
    key_id='<your_client_key_id>',
    key_secret='<your_client_secret_key>',
    webhook_secret='<your_webhook_secret_key>',
    use_sandbox=True  # Set to False when moving to production
)
payment_info = PaymentInfo(
    key_id=skipcash.key_id,
    amount=Decimal('100.00'),
    first_name='John',
    last_name='Doe',
    phone='+1234567890',
    email='john.doe@example.com',
    street='123 Main St',
    city='City',
    state='ST',
    country='Country',
    postal_code='00000',
    transaction_id='unique_transaction_id',
    custom_fields={'Custom1': 'value1', 'Custom2': 'value2'}  # Optional
)

payment = Payment(skipcash)

try:
    response = payment.create_payment(payment_info)
    print(f"Payment ID: {response.id}")
    print(f"Payment URL: {response.pay_url}")
except PaymentInfoError as e:
    print(f"Error: {e}")
except PaymentValidationError as e:
    print(f"Validation Error: {e}")
except PaymentResponseError as e:
    print(f"Response Error: {e}")
```

### Retrieving a Payment

To retrieve payment details using a payment ID:

```python
from skipcash.client import SkipCash
from skipcash.exceptions import PaymentRetrievalError, PaymentResponseError
from skipcash.api_resources import Payment

skipcash = SkipCash(
    client_id='<your_client_id>',
    key_id='<your_client_key_id>',
    key_secret='<your_client_secret_key>',
    webhook_secret='<your_webhook_secret_key>',
    use_sandbox=True  # Set to False when moving to production
)
payment = Payment(skipcash)
try:
    response = payment.get_payment('<payment_id>')
    print(f"Payment ID: {response.id}")
    print(f"Payment Status: {response.status}")
except PaymentRetrievalError as e:
    print(f"Retrieval Error: {e}")
except PaymentResponseError as e:
    print(f"Response Error: {e}")
```

### Handling Webhooks

To validate and process webhook events:

```python
from skipcash.client import SkipCash
from skipcash.api_resources import Webhook
from skipcash.exceptions import WebhookValidationError, WebhookSignatureError

request_data = {}  # Your webhook payload here
signature = ''  # Signature from the 'HTTP_AUTHORIZATION' header
skipcash = SkipCash(
    client_id='<your_client_id>',
    key_id='<your_client_key_id>',
    key_secret='<your_client_secret_key>',
    webhook_secret='<your_webhook_secret_key>',
    use_sandbox=True  # Set to False when moving to production
)
webhook = Webhook(client=skipcash)

try:
    webhook.validate(payload=request_data, signature=signature)
    webhook_response = webhook.process_event(request_data)
    print(f"Payment ID: {webhook_response.payment_id}")
    print(f"Payment Status: {webhook_response.status}")
except WebhookValidationError as e:
    print(f"Webhook Validation Error: {e}")
except WebhookSignatureError as e:
    print(f"Webhook Signature Error: {e}")
```

## Error Handling

The SDK raises specific exceptions to help you handle errors gracefully. These exceptions include `PaymentResponseError`, `PaymentValidationError`, `PaymentInfoError`, `PaymentRetrievalError`, `WebhookValidationError`, and `WebhookSignatureError`.

