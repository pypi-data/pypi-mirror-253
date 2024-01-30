import json
import os
from typing import IO, Optional, Union

import requests
from requests.exceptions import HTTPError

from coinbase import jwt_generator
from coinbase.__version__ import __version__
from coinbase.api_base import APIBase
from coinbase.constants import API_ENV_KEY, API_SECRET_ENV_KEY, BASE_URL


def handle_exception(response):
    """Raises :class:`HTTPError`, if one occurred."""

    http_error_msg = ""
    reason = response.reason

    if 400 <= response.status_code < 500:
        if (
            response.status_code == 403
            and '"error_details":"Missing required scopes"' in response.text
        ):
            http_error_msg = f"{response.status_code} Client Error: Missing Required Scopes. Please verify your API keys include the necessary permissions."
        else:
            http_error_msg = (
                f"{response.status_code} Client Error: {reason} {response.text}"
            )
    elif 500 <= response.status_code < 600:
        http_error_msg = (
            f"{response.status_code} Server Error: {reason} {response.text}"
        )

    if http_error_msg:
        raise HTTPError(http_error_msg, response=response)


class RESTBase(APIBase):
    def __init__(
        self,
        api_key: Optional[str] = os.getenv(API_ENV_KEY),
        api_secret: Optional[str] = os.getenv(API_SECRET_ENV_KEY),
        key_file: Optional[Union[IO, str]] = None,
        base_url=BASE_URL,
        timeout=None,
    ):
        super().__init__(
            api_key=api_key,
            api_secret=api_secret,
            key_file=key_file,
            base_url=base_url,
            timeout=timeout,
        )

    def get(self, url_path, params: Optional[dict] = None, **kwargs):
        params = params or {}

        if kwargs:
            params.update(kwargs)

        return self.prepare_and_send_request("GET", url_path, params, data=None)

    def post(
        self,
        url_path,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        **kwargs,
    ):
        data = data or {}

        if kwargs:
            data.update(kwargs)

        return self.prepare_and_send_request("POST", url_path, params, data)

    def put(
        self,
        url_path,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        **kwargs,
    ):
        data = data or {}

        if kwargs:
            data.update(kwargs)

        return self.prepare_and_send_request("PUT", url_path, params, data)

    def delete(
        self,
        url_path,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
        **kwargs,
    ):
        data = data or {}

        if kwargs:
            data.update(kwargs)

        return self.prepare_and_send_request("DELETE", url_path, params, data)

    def prepare_and_send_request(
        self,
        http_method,
        url_path,
        params: Optional[dict] = None,
        data: Optional[dict] = None,
    ):
        headers = self.set_headers(http_method, url_path)

        if params is not None:
            params = {key: value for key, value in params.items() if value is not None}

        if data is not None:
            data = {key: value for key, value in data.items() if value is not None}

        return self.send_request(http_method, url_path, params, headers, data=data)

    def send_request(self, http_method, url_path, params, headers, data=None):
        if data is None:
            data = {}

        url = f"https://{self.base_url}{url_path}"

        response = requests.request(
            http_method,
            url,
            params=params,
            json=data,
            headers=headers,
            timeout=self.timeout,
        )
        handle_exception(response)  # Raise an HTTPError for bad responses

        return response.json()

    def set_headers(self, method, path):
        uri = f"{method} {self.base_url}{path}"
        jwt = jwt_generator.build_rest_jwt(uri, self.api_key, self.api_secret)
        return {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + jwt,
            "User-Agent": "coinbase-advanced-py/" + __version__,
        }
