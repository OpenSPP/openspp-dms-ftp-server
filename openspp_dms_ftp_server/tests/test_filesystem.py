from urllib.request import FTPHandler

from ..filesystems import OpenSPPFS


class TestOpenSPPFS:
    def test_file_open(self):
        filename = "tests/test_handlers.py"
        fs = OpenSPPFS("/home/root/", FTPHandler)
        opened_file = fs.open(filename, "wb")
        assert filename != opened_file.name
        assert filename.replace("/", "_") in opened_file.name

    def test_dir_listing(self):
        filename = "tests/test_handlers.py"
        fs = OpenSPPFS("/home/root/", FTPHandler)
        dirs = fs.listdir(filename)
        assert [] == dirs

        dirs2 = fs.listdir("")
        assert [] == dirs2
