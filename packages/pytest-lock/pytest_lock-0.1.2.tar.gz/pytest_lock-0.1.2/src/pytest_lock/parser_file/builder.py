from typing import Dict

from pytest_lock.parser_file.base import ParserFile
from pytest_lock.parser_file.json import ParserFileJson


class ParserFileBuilder:
    """
    Builder for ParserFile

    Attributes:
        mapping: Mapping of extension and ParserFile
    """

    mapping: Dict[str, ParserFile]

    def __init__(self):
        self.mapping = {
            ".json": ParserFileJson(),
        }

    def build(self, extension: str = ".json") -> ParserFile:
        """
        Build a ParserFile from extension

        Args:
            extension: Extension of file to build ParserFile
        """
        parser_file = self.mapping.get(extension)

        if parser_file is None:
            raise ValueError("No parser_file file found")

        return parser_file
