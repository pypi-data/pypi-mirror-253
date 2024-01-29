from skipcash.utils import HttpClient


class SkipCash:
    """

    SkipCash
    ========

    A class for interacting with the SkipCash API.

    .. py:class:: SkipCash(client_id, key_id, key_secret, webhook_secret, use_sandbox=True)

       Initializes a new instance of the SkipCash class.

       :param client_id: The client ID for authentication.
       :type client_id: str
       :param key_id: The key ID for authentication.
       :type key_id: str
       :param key_secret: The key secret for authentication.
       :type key_secret: str
       :param webhook_secret: The webhook secret for authentication.
       :type webhook_secret: str
       :param use_sandbox: Determines whether to use the sandbox environment or the production environment. Defaults to True.
       :type use_sandbox: bool

    .. py:attribute:: SANDBOX_URL

       The base URL for the SkipCash sandbox environment.

       :type: str

    .. py:attribute:: PRODUCTION_URL

       The base URL for the SkipCash production environment.

       :type: str

    .. py:method:: post(endpoint, data)

       Sends a POST request to the specified endpoint with the provided data.

       :param endpoint: The API endpoint to send the request to.
       :type endpoint: str
       :param data: The data to include in the request body.
       :type data: dict
       :return: The response from the API.
       :rtype: HttpResponse

    .. py:method:: get(endpoint)

       Sends a GET request to the specified endpoint.

       :param endpoint: The API endpoint to send the request to.
       :type endpoint: str
       :return: The response from the API.
       :rtype: HttpResponse

    """
    SANDBOX_URL = "https://skipcashtest.azurewebsites.net"
    PRODUCTION_URL = "https://api.skipcash.app"

    def __init__(self, client_id, key_id, key_secret, webhook_secret, use_sandbox=True):
        self.client_id = client_id
        self.key_id = key_id
        self.key_secret = key_secret
        self.webhook_secret = webhook_secret
        base_url = self.SANDBOX_URL if use_sandbox else self.PRODUCTION_URL
        self.http_client = HttpClient(base_url, self.key_secret, self.client_id)

    def post(self, endpoint, data):
        return self.http_client.post(endpoint, data)

    def get(self, endpoint):
        return self.http_client.get(endpoint)

