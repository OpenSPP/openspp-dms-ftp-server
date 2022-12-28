from pyftpdlib.authorizers import DummyAuthorizer

from . import TypeHandler
from .clients import OpenSPPClient


class OpenSPPAuthorizer(DummyAuthorizer):
    """
    Custom Authorizer with OpenSPP method for login
    """

    def validate_authentication(
        self, username: str, password: str, handler: type[TypeHandler]
    ) -> None:
        """
        Login to OpenSPP to check if user is valid.
        :param username: User's username with upload permission
        :param password: API key or password of the user
        :param handler: Auth handler
        """
        openspp_client = OpenSPPClient()
        openspp_client.login(username=username, password=password)

    def get_perms(self, username: str) -> str:
        """
        Return current user permissions.
        :param username: User's username with upload permission
        :return: Empty string. We don't view the user permission of OpenSPP here
        """
        return ""

    def get_home_dir(self, username: str) -> str:
        """
        Get the home directory of the user
        :param username: User's username with upload permission
        :return: Empty string. We don't have a home directory.
        """
        return ""

    def has_perm(self, username: str, perm: str, path: str | None = None) -> bool:
        """
        Check user if it can log in to OpenSPP has permissions.
        :param username: User's username with upload permission
        :param perm: User's permission
        :param path: Directory path to check permission
        :return: Always returns True
        """

        return True

    def get_msg_login(self, username: str) -> str:
        """
        Get the message to show after logging in.
        :param username: User's username with upload permission
        """
        return ""

    def add_user(
        self,
        **kwargs,
    ) -> None:
        """
        Adding user to the database. We don't allow it since our users will be based on OpenSPPS
        :param kwargs:
        :raise: Exception
        """
        raise Exception("Action not allowed.")

    def add_anonymous(self, homedir, **kwargs) -> None:
        """
        Adding anonymous user to the database. We don't allow it since our users will be based on OpenSPP
        :param kwargs:
        :raise: Exception
        """
        raise Exception("Action not allowed.")
