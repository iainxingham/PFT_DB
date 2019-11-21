# Base class for various report parsers

from tika import parser
from os import path
from enum import Enum, unique, auto
import re

@unique
class ParseError(Enum):
    PARSE_OK = auto()
    PARSE_NO_FILE = auto()

class BaseParse:
    def __init__(self, file: str):
        self.extracted = dict()
        self.source_file = file
        if path.exists(file):
            data = parser.from_file(file)
            self.text = data['content']
            self.error_code = ParseError.PARSE_OK
        else:
            self.error_code = ParseError.PARSE_NO_FILE

    def is_ok(self) -> bool:
        if self.error_code is ParseError.PARSE_OK:
            return True
        else:
            return False

    def _add_extract(self, key: str, regex: str, group: int):
        result = re.compile(regex).search(self.text)
        if result is None:
            self._log('Unable to extract \"{0}\" from {1}\n'.format(key, self.source_file))
        else:
            self.extracted[key] = result.group(group)

    def _log(self, msg: str):
        pass

    
