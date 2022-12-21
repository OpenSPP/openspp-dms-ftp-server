import io

from pyftpdlib.filesystems import AbstractedFS


class OpenSPPFS(AbstractedFS):
    """
    Custom FileSystem class for handling the filesystem based on OpenSPP use-cases
    """

    def open(self, filename: str, mode: str) -> io.BytesIO:
        """
        Custom open function to return file from memory.
        :param filename: Name of file to be uploaded
        :param mode: Mode of opening a file
        :return: An instance of BytesIO representing the file opened
        """
        dir_tree = filename.split("/")
        new_filename = "_".join(dir_tree)
        # Save file to memory instead of saving it to filesystem
        in_mem_file = io.BytesIO(initial_bytes=b"")
        in_mem_file.name = new_filename
        return in_mem_file

    def listdir(self, path: str) -> list:
        """Don't return anything."""
        return []
