from unittest.mock import patch

import pytest

from ..authorizers import OpenSPPAuthorizer
from ..handlers import OpenSPPFTPHandler


class TestOpenSPPAuthorizer:
    def setup_method(self, setup_method):
        self.username = "sampleuser"
        self.password = "password"
        self.authorizer = OpenSPPAuthorizer()

    @patch("clients.OpenSPPClient.login")
    def test_authentication(self, mock_client):
        mock_client = mock_client.return_value
        mock_client.login.return_value = True

        response = self.authorizer.validate_authentication(
            username=self.username, password=self.password, handler=OpenSPPFTPHandler
        )
        assert response is None

    def test_permission(self):
        assert self.authorizer.get_perms(self.username) == ""
        assert self.authorizer.has_perm(self.authorizer, "elw") is True

    def test_home_dir(self):
        assert self.authorizer.get_home_dir(self.username) == ""

    def test_message_login(self):
        assert self.authorizer.get_msg_login(self.username) == ""

    def test_add_user(self):
        with pytest.raises(Exception) as e_info:
            self.authorizer.add_user()

        assert "Action not allowed." in str(e_info)

        with pytest.raises(Exception) as e_info2:
            self.authorizer.add_anonymous(homedir=".")

        assert "Action not allowed." in str(e_info2)
