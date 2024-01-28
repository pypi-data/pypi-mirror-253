from abc import ABC, abstractmethod
from pathlib import Path

from pytest_lock.models.cache.file import FileCache


class ParserFile(ABC):
    """
    Base class for parser file.

    Attributes:
        encoding: Encoding of file
    """

    def __init__(self, encoding: str = "utf-8"):
        self.encoding = encoding

    @abstractmethod
    def read_file(self, path: Path) -> FileCache:
        """
        Read a file and return the content with format waited

        Args:
            path: Path of file to extract content

        Returns:
            content of file with format FileCache
        """

    @abstractmethod
    def write_file(self, path: Path, file_cache: FileCache) -> None:
        """
        Write a file with content with format waited

        Args:
            path: Path of file to write content
            file_cache: Content of file with format FileCache
        """
