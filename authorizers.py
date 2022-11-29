import tempfile

from pyftpdlib.authorizers import DummyAuthorizer

from client import OpenSPPClient
from config import OPENSPP_DB_NAME, OPENSPP_URL


class OpenSPPAuthorizer(DummyAuthorizer):
    def openspp_login(self, username, password):
        client = OpenSPPClient(
            db_name=OPENSPP_DB_NAME,
            username=username,
            password=password,
            server_root=OPENSPP_URL,
        )
        uid = client.login()
        if not uid:
            raise Exception("No user")
        return uid

    def add_user(
        self,
        username,
        password,
        perm="elr",
        msg_login="Login successful.",
        msg_quit="Goodbye.",
        **kwargs,
    ):
        uid = self.openspp_login(username, password)

        # TODO: Change this to in-memory filehandler. We don't want to save the files in the FS
        dir_name = f"{uid}-{username}"
        temp_dir = tempfile.TemporaryDirectory(prefix=dir_name)
        super().add_user(
            username=username,
            password=password,
            homedir=temp_dir.name,
            perm=perm,
            msg_login=msg_login,
            msg_quit=msg_quit,
        )

    def add_anonymous(self, homedir, **kwargs):
        raise Exception("Action not allowed.")
