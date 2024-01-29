import uuid
from decimal import Decimal
from typing import Dict, Any

from skipcash.exceptions import PaymentInfoError
from skipcash.utils import is_valid_country, is_valid_uuid


class FieldDescriptor:
    def __init__(self, name, required=False, max_length=None, decimal=False):
        self.name = name
        self.required = required
        self.max_length = max_length
        self.decimal = decimal

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__.get(self.name)

    def __set__(self, instance, value):
        if value is None and self.required:
            raise PaymentInfoError("{} is required".format(self.name.capitalize()))
        if self.max_length and len(str(value)) > self.max_length:
            raise PaymentInfoError("{} exceeds maximum length of {} characters".format(self.name.capitalize(), self.max_length))
        if self.decimal and (value < Decimal('0.00') or value.as_tuple().exponent < -2):
            raise PaymentInfoError("{} must be non-negative with up to two decimal places".format(self.name.capitalize()))
        instance.__dict__[self.name] = value


class PaymentInfo:
    """Class representing payment information for a transaction.

    Parameters:
        key_id (str): The key identifier for the payment.
        amount (Decimal): The amount to be paid.
        first_name (str): The first name of the customer.
        last_name (str): The last name of the customer.
        phone (str): The phone number of the customer.
        email (str): The email address of the customer.
        street (str): The street address of the customer.
        city (str): The city of the customer.
        transaction_id (str): The transaction ID.
        state (str, optional): The state of the customer. Defaults to 'QA'.
        country (str, optional): The country of the customer. Defaults to 'QA'.
        postal_code (str, optional): The postal code of the customer. Defaults to '00000'.
        **custom_fields: Additional custom fields for the transaction.

    Attributes:
        key_id (str): The key identifier for the payment.
        amount (Decimal): The amount to be paid.
        first_name (str): The first name of the customer.
        last_name (str): The last name of the customer.
        phone (str): The phone number of the customer.
        email (str): The email address of the customer.
        street (str): The street address of the customer.
        city (str): The city of the customer.
        state (str): The state of the customer.
        country (str): The country of the customer.
        postal_code (str): The postal code of the customer.
        transaction_id (str): The transaction ID.
        custom_fields (dict): Additional custom fields for the transaction.

    """
    key_id = FieldDescriptor('key_id', required=True)
    amount = FieldDescriptor('amount', required=True, decimal=True)
    first_name = FieldDescriptor('first_name', required=True, max_length=60)
    last_name = FieldDescriptor('last_name', required=True, max_length=60)
    phone = FieldDescriptor('phone', required=True, max_length=15)
    email = FieldDescriptor('email', required=True, max_length=255)
    street = FieldDescriptor('street', required=True, max_length=60)
    city = FieldDescriptor('city', required=True, max_length=50)
    state = FieldDescriptor('state', required=True, max_length=2)
    country = FieldDescriptor('country', required=True, max_length=2)
    postal_code = FieldDescriptor('postal_code', required=True, max_length=10)
    transaction_id = FieldDescriptor('transaction_id', required=True, max_length=40)

    def __init__(self, key_id, amount, first_name, last_name, phone, email, street, city, transaction_id, state='QA', country='QA', postal_code='00000', **custom_fields):
        self.key_id = key_id
        self.amount = amount
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.email = email
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.postal_code = postal_code
        self.transaction_id = transaction_id
        self.custom_fields = {}
        # Directly assign custom fields without nesting them
        if len(custom_fields) > 0 and isinstance(custom_fields, dict) and 'custom_fields' in custom_fields:
            for field_name, field_value in custom_fields['custom_fields'].items():
                self.custom_fields.update({field_name: field_value})

    def validate(self):
        """
        Validates the key ID, country, and custom fields.

        :return: None
        """
        self.validate_key_id()
        self.validate_country()
        self.validate_custom_fields()

    def validate_country(self):
        """
        Validates the country ISO code.

        :return: None
        :raises: PaymentInfoError - if the country ISO code is not valid.
        """
        if not is_valid_country(self.country):
            raise PaymentInfoError("Please provide a valid country ISO code")

    def validate_key_id(self):
        """Validates the key_id parameter.

            :return: None
            :raises PaymentInfoError: If the key_id is not a valid UUID string.
        """
        if not is_valid_uuid(self.key_id):
            raise PaymentInfoError("Please provide a valid UUID string as key_id")

    def validate_custom_fields(self):
        """
        Validates the custom fields.

        :return: None
        """
        if len(self.custom_fields.items()) > 0:
            if len(self.custom_fields.items()) > 10:
                raise PaymentInfoError("Only 10 custom fields are allowed")

            for i, key in enumerate(self.custom_fields.keys(), start=1):
                expected_key = "Custom{}".format(i)
                if key != expected_key:
                    raise PaymentInfoError("Keys must be in order and should start with name Custom1.")

            for key, field_value in self.custom_fields.items():
                if len(field_value) > 50:
                    raise PaymentInfoError("Value for key '{}' in custom_fields should not exceed 50 characters".format(key))

    def to_skipcash_dict(self) -> Dict[str, Any]:
        """

        Converts the information from the current object instance into a dictionary format that is compatible with the SkipCash API.

        :return: A dictionary containing the information from the current object instance.
        :rtype: dict

        """
        random_uuid = uuid.uuid4()
        postData = {
            "Uid": str(random_uuid),
            "KeyId": str(self.key_id),
            "Amount": "{:.2f}".format(self.amount),
            "FirstName": self.first_name,
            "LastName": self.last_name,
            "Phone": self.phone,
            "Email": self.email,
            "Street": self.street,
            "City": self.city,
            "State": self.state,
            "Country": self.country,
            "PostalCode": self.postal_code,
            "TransactionId": self.transaction_id,
        }
        if len(self.custom_fields.items()) > 0:
            for k, v in self.custom_fields.items():
                postData.update({k: v})
        return postData
