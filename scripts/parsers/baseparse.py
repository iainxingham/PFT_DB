# Base class for various report parsers

from tika import parser
from os import path
from enum import Enum, unique, auto

@unique
class ParseError(Enum):
    PARSE_OK = auto()
    PARSE_NO_FILE = auto()

class BaseParse:
    def __init__(self, file: str):
        self.extracted = dict()
        if path.exists(file):
            data = parser.from_file(file)
            self.text = data['content']
            self.error_code = ParseError.PARSE_OK
        else:
            self.error_code = ParseError.PARSE_NO_FILE

    
