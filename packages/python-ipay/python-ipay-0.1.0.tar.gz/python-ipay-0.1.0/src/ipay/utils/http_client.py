from requests import post, get, patch, put, delete, request
import requests


class HttpClient:
    """
    This class is used to make http requests.
    """

    def __init__(self, base_url: str, headers: dict = None):
        """
        This is the constructor method for the HttpRequest class.
        Args:
            base_url (str): The base url to be used for the requests.
            headers (dict): The headers to be used for the requests.
        """
        self.base_url = base_url
        self.headers = headers

    def get(self, url: str, params: dict = None, headers: dict = None):
        """
        This method is used to make a get request.
        Args:
            url (str): The url to be used for the request.
            params (dict): The params to be used for the request.
            headers (dict): The headers to be used for the request.
        Returns:
            requests.Response: The response object from the request.
        """
        return get(url=f"{self.base_url}{url}", params=params, headers=headers)

    def post(self, url: str, data: dict = None, headers: dict = None):
        """
        This method is used to make a post request.
        Args:
            url (str): The url to be used for the request.
            data (dict): The data to be used for the request.
            headers (dict): The headers to be used for the request.
        Returns:
            requests.Response: The response object from the request.
        """
        return post(url=f"{self.base_url}{url}", data=data, headers=headers)

    def put(self, url: str, data: dict = None, headers: dict = None):
        """
        This method is used to make a put request.
        Args:
            url (str): The url to be used for the request.
            data (dict): The data to be used for the request.
            headers (dict): The headers to be used for the request.
        Returns:
            requests.Response: The response object from the request.
        """
        return put(url=f"{self.base_url}{url}", data=data, headers=headers)

    def patch(self, url: str, data: dict = None, headers: dict = None):
        """
        This method is used to make a patch request.
        Args:
            url (str): The url to be used for the request.
            data (dict): The data to be used for the request.
            headers (dict): The headers to be used for the request.
        Returns:
            requests.Response: The response object from the request.
        """
        return patch(url=f"{self.base_url}{url}", data=data, headers=headers)

    def delete(self, url: str, data: dict = None, headers: dict = None):
        """
        This method is used to make a delete request.
        Args:
            url (str): The url to be used for the request.
            data (dict): The data to be used for the request.
            headers (dict): The headers to be used for the request.
        Returns:
            requests.Response: The response object from the request.
        """
        return delete(url=f"{self.base_url}{url}", data=data, headers=headers)

    def request(self, method: str, url: str, params: dict = None, data: dict = None, headers: dict = None):
        """
        This method is used to make a request.
        Args:
            method (str): The method to be used for the request.
            url (str): The url to be used for the request.
            params (dict): The params to be used for the request.
            data (dict): The data to be used for the request.
            headers (dict): The headers to be used for the request.
        Returns:
            requests.Response: The response object from the request.
        """
        return request(method=method, url=f"{self.base_url}{url}", params=params, data=data, headers=headers)
