import codecs
import logging

import requests

from config.base import OPENSPP_URL

logger = logging.getLogger(__name__)


class OpenSPPClientException(Exception):
    pass


class OpenSPPClient:
    """
    Base client for OpenSPP communications
    """

    def login(self, username: str, password: str) -> bool:
        """
        Call OpenSPP login endpoint to make sure the credentials are valid.
        :param username: User's username with upload permission
        :param password: API key or password of the user
        :return: Returns True if the user is valid
        """

        url = f"{OPENSPP_URL}/dms/auth"
        payload = {
            "params": {
                "username": username,
                "password": password,
            }
        }
        response = requests.post(
            url=url, json=payload, headers={"Content-Type": "application/json"}
        )
        response_content = response.json()
        if response.status_code != 200:
            raise OpenSPPClientException(
                f"Unsuccessful login. Response data: {response_content}"
            )

        result = response_content.get("result", "")
        if "200 OK" not in result:
            raise OpenSPPClientException(
                f"Unsuccessful login. Response data: {response_content}"
            )
        return True

    def upload_file(self, username: str, password: str, filename: str) -> None:
        """
        Call OpenSPP upload endpoint to save the file.
        :param username: User's username with upload permission
        :param password: API key or password of the user
        :param filename: Name of file for upload
        """
        with open(filename, "rb") as read_file:
            base_filename = filename.split("/")[-1]
            data = read_file.read()
            file_content = codecs.encode(data, "base64").decode("utf-8")

        url = f"{OPENSPP_URL}/dms/upload/"
        payload = {
            "params": {
                "username": username,
                "password": password,
                "filename": base_filename,
                "file": file_content,
            }
        }
        response = requests.post(
            url=url, json=payload, headers={"Content-Type": "application/json"}
        )
        response_content = response.json()
        if response.status_code != 200:
            logger.info(
                f"Something went wrong during file upload. Response data: {response_content}"
            )
        result = response_content.get("result", "")
        if "200 OK" not in result:
            logger.info(
                f"Something went wrong during file upload. Response data: {response_content}"
            )
