# Read oximetry - report from older device

import scripts.parsers.baseparse as baseparse
import re

class OldOxiParse(baseparse.BaseParse):
    def __init__(self, file: str):
        super().__init__(file)

        if self.error_code is baseparse.ParseError.PARSE_OK:
            self.extract() 

    def extract(self):
        self._add_extract('RXR', r'Index Number:[\s]*(((rxr)|(RXR))(\d){7})', 1)
        self._add_extract('date', r'Date of Study:[\s]*(\d{1,2}[\\/\.:]\d{1,2}[\\/\.:]\d{2,4})', 1)
        self._add_extract('dob', r'Date of Birth:[\s]*(\d{1,2}[\\/\.:]\d{1,2}[\\/\.:]\d{2,4})', 1)

        self._add_extract('odi', r'Average Dips/Hour: (\d{1,3}\.?\d{0,2})[\s]*\(\>=4\%\)', 1)
        self._add_extract('hri', r'Rises/Hr:[\s]*(\d{1,3}\.?\d{0,2})[\s]*\(\>6bpm\)', 1)

        re_name = re.compile(r'Patient Name:[\s]*([A-Za-z]+)[\s]*,[\s]*([A-Za-z]+)').search(self.text)
        if re_name is None:
            self._log('No name extracted from {0}\n'.format(self.source_file))
        else:
            self.extracted['fname'] = re_name.group(2).lower().capitalize()  # First name
            self.extracted['lname'] = re_name.group(1).lower().capitalize()  # Surname
