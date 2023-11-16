from unittest.mock import patch

import pytest

from openspp_dms_ftp_server.clients import OpenSPPClient, OpenSPPClientException
from openspp_dms_ftp_server.tests.mock_objects import MockResponse


class TestOpenSPPClient:
    def setup_method(self, setup_method):
        self.username = "sampleuser"
        self.password = "password"
        self.clients = OpenSPPClient()

    @patch("openspp_dms_ftp_server.clients.requests.post")
    def test_authentication(self, mock_client):
        mock_client.return_value = MockResponse(
            status_code=200,
            json_={"result": "200 OK"},
            headers={"Content-Type": "application/json"},
        )

        response = self.clients.login(username=self.username, password=self.password)
        assert response is True

    @patch("openspp_dms_ftp_server.clients.requests.post")
    def test_invalid_authentication(self, mock_client):
        mock_client.return_value = MockResponse(status_code=400)

        with pytest.raises(OpenSPPClientException):
            self.clients.login(username=self.username, password=self.password)

    @patch("openspp_dms_ftp_server.clients.requests.post")
    def test_unsuccessful_authentication(self, mock_client):
        mock_client.return_value = MockResponse(
            status_code=200, json_={"result": "Unsuccessful"}
        )

        with pytest.raises(OpenSPPClientException):
            self.clients.login(username=self.username, password=self.password)
