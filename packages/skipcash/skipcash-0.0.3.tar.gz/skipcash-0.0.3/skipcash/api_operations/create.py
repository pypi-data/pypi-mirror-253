def create(client, endpoint, data):
    """
    :param client: The client object used to make the POST request.
    :param endpoint: The endpoint to which the POST request will be made.
    :param data: The data to be sent with the POST request.
    :return: The response from the POST request.

    """
    return client.post(endpoint, data)