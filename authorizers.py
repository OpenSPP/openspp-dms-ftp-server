from pyftpdlib.authorizers import DummyAuthorizer

from clients import OpenSPPClient


class OpenSPPAuthorizer(DummyAuthorizer):
    """
    Custom Authorizer with OpenSPP method for login
    """

    def validate_authentication(self, username, password, handler):
        openspp_client = OpenSPPClient()
        openspp_client.login(username=username, password=password)

    def get_home_dir(self, username):
        return ""

    def has_perm(self, username, perm, path=None):
        return True

    def get_msg_login(self, username):
        return ""

    def add_user(
        self,
        **kwargs,
    ):
        raise Exception("Action not allowed.")

    def add_anonymous(self, homedir, **kwargs):
        raise Exception("Action not allowed.")
