import hmac
import hashlib
import base64


def generate_signature(api_key, data):
    """
    :param api_key: The API key used for generating the signature.
    :param data: A dictionary containing the data to be included in the signature. The dictionary should have the mandatory fields in the specified order.
    :return: The generated signature encoded in base64.

    This method generates a signature using the provided API key and data. The data should contain all the mandatory fields in the specified order. Optional fields can also be included in
    * the data dictionary. The signature is generated using HMAC SHA256 algorithm.

    Example usage:
        api_key = "API_KEY_HERE"
        data = {
            "Uid": "123456789",
            "KeyId": "KEY_ID",
            "Amount": 100,
            "FirstName": "John",
            "LastName": "Doe",
            "Phone": "1234567890",
            "Email": "john.doe@example.com",
            "Street": "123 Main St",
            "City": "New York",
            "State": "NY",
            "Country": "USA",
            "PostalCode": "12345",
            "TransactionId": "1234567890"
        }

        signature = generate_signature(api_key, data)
        print(signature)
    """
    # Define the mandatory fields in the specified order
    field_order = [
        "Uid",
        "KeyId",
        "Amount",
        "FirstName",
        "LastName",
        "Phone",
        "Email",
        "Street",
        "City",
        "State",
        "Country",
        "PostalCode",
        "TransactionId"
    ]
    mandatory_parts = ['{}={}'.format(field, data[field]) for field in field_order if field in data and data.get(field)]
    optional_parts = ['{}={}'.format(key, value) for key, value in data.items() if key not in field_order and value]
    if len(optional_parts) > 0:
        # If many specified use only one (1st) in the signature
        message = ','.join(mandatory_parts) + ',' + optional_parts[0]
    else:
        message = ','.join(mandatory_parts)

    # Generate HMAC SHA256 signature
    signature = hmac.new(api_key.encode(), message.encode(), hashlib.sha256).digest()
    encoded_signature = base64.b64encode(signature).decode()

    return encoded_signature


def validate_signature(payload, signature, secret):
    """
    :param payload: dictionary containing the payload data
    :param signature: the signature to validate
    :param secret: the secret key used to generate the signature
    :return: True if the signature is valid, False otherwise

    This method validates the signature of a payload using the HMAC SHA256 algorithm with the provided secret key. It compares the provided signature with the calculated signature for the
    * payload. The payload is expected to be a dictionary containing key-value pairs.

    The mandatory fields to include in the signature calculation are defined in the 'field_order' list, which specifies the order in which these fields should be concatenated. Only fields
    * that exist in the payload and have a non-empty value will be included in the calculation.

    The method constructs a message string by concatenating the mandatory fields and their values, separated by commas. It then generates the HMAC SHA256 signature by hashing the message
    * using the secret key. The resulting signature is base64 encoded.

    The method returns True if the provided signature matches the calculated signature, indicating that the payload's integrity is intact. Otherwise, it returns False.
    """
    # Define the mandatory fields in the specified order
    field_order = [
        "PaymentId",
        "Amount",
        "StatusId",
        "TransactionId",
        "Custom1",
        "VisaId",
    ]
    mandatory_parts = ['{}={}'.format(field, payload[field]) for field in field_order if field in payload and payload.get(field)]
    message = ','.join(mandatory_parts)
    # Generate HMAC SHA256 signature
    data_signature = hmac.new(secret.encode(), message.encode(), hashlib.sha256).digest()
    encoded_signature = base64.b64encode(data_signature).decode()
    return signature == encoded_signature



