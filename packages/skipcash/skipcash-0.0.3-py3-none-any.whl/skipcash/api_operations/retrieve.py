def retrieve(client, endpoint):
    """Retrieve data from the specified endpoint.

    :param client: The client object used to make the request.
    :param endpoint: The endpoint from which the data should be retrieved.
    :return: The retrieved data.
    """
    return client.get(endpoint)