from skipcash.exceptions import WebhookValidationError


def validation_required(method):
    """
    Decorator that checks if the instance has been validated before executing the given method.

    :param method: The method to be validated.
    :return: A wrapper function that performs the validation check.
    """
    def wrapper(instance, *args, **kwargs):
        if not getattr(instance, '_is_validated', False):
            raise WebhookValidationError(f"Please call validate method before calling {method.__name__}.")
        return method(instance, *args, **kwargs)
    return wrapper
