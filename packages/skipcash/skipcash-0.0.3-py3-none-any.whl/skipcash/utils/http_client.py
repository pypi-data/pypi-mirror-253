import requests
from .signature import generate_signature


class HttpClient:
    """
    The HttpClient class provides methods to make HTTP requests to an API.

    :param base_url: The base URL of the API.
    :param api_key: The API key for authentication.
    :param client_id: The client ID for authorization.

    :ivar base_url: The base URL of the API.
    :ivar api_key: The API key for authentication.
    :ivar client_id: The client ID for authorization.
    """
    def __init__(self, base_url, api_key, client_id):
        self.base_url = base_url
        self.api_key = api_key
        self.client_id = client_id

    def post(self, endpoint, data):
        """
        Sends a POST request to the specified endpoint with the provided data.

        :param endpoint: The relative URL endpoint to which the request will be sent.
        :type endpoint: str
        :param data: The data to be included in the request body.
        :type data: dict
        :return: The response from the server.
        :rtype: requests.Response
        """
        url = "{}{}".format(self.base_url, endpoint)
        signature = generate_signature(self.api_key, data)
        headers = {'Authorization': signature}
        return requests.post(url, json=data, headers=headers)

    def get(self, endpoint):
        """
        Performs a GET request to the specified endpoint.

        :param endpoint: The API endpoint to send the GET request to.
        :type endpoint: str
        :return: The response from the GET request.
        :rtype: requests.Response
        """
        url = "{}{}".format(self.base_url, endpoint)
        headers = {'Authorization': self.client_id}
        return requests.get(url, headers=headers)