import uuid
import pycountry
from decimal import Decimal, InvalidOperation


def is_valid_country(country_code):
    """
    :param country_code: The two-letter country code to check for validity.
    :return: True if the country code is valid, False otherwise.
    """
    try:
        country = pycountry.countries.get(alpha_2=country_code)
        return True if country else False
    except KeyError:
        return False


def is_valid_uuid(uuid_to_test, version=4):
    """
    Validate if a given string is a valid UUID.

    :param uuid_to_test: A string representing the UUID to be validated.
    :param version: An integer representing the UUID version to be validated against. Default is version 4.
    :return: A boolean value indicating if the given string is a valid UUID.

    Example usage:
    >>> is_valid_uuid('123e4567-e89b-12d3-a456-426614174000')
    True

    >>> is_valid_uuid('not a uuid')
    False

    >>> is_valid_uuid('123e4567-e89b-12d3-a456-426614174000', version=4)
    True

    >>> is_valid_uuid('123e4567-e89b-12d3-a456-426614174000', version=5)
    False
    """
    try:
        uuid_obj = uuid.UUID(uuid_to_test, version=version)
        return str(uuid_obj) == uuid_to_test
    except ValueError:
        return False


def is_decimal_with_max_two_places(value):
    """Function to check if a value is a decimal with a maximum of two decimal places.

    :param value: The value to check.
    :return: True if the value is a decimal with a maximum of two decimal places, False otherwise.
    """
    try:
        decimal_value = Decimal(value)
        return decimal_value == decimal_value.quantize(Decimal('1.00')) or decimal_value.as_tuple().exponent >= -2
    except (InvalidOperation, ValueError):
        return False

