import xmlrpc.client


class OpenSPPClient:
    COMMON_ENDPOINT = "/xmlrpc/2/common"

    def __init__(self, server_root: str, username: str, password: str, db_name: str):
        """Initialize a PDS SPP client.

        :param server_root: PDS SPP root url. E.g: https://dev.newlogic-demo.com/
        :param username: User's username with access to the server
        :param password: User's password or API key with access to the server
        :param db_name: Name of database that contains the data for query
        :return: a PDSSPPClient instance.
        """
        self.server_root = server_root
        self.username = username
        self.password = password
        self.db_name = db_name

    @staticmethod
    def get_server_proxy(url):
        return xmlrpc.client.ServerProxy(url)

    def login(self):
        common_endpoint = self.get_server_proxy(
            f"{self.server_root}{self.COMMON_ENDPOINT}"
        )
        return common_endpoint.authenticate(
            self.db_name, self.username, self.password, {}
        )
