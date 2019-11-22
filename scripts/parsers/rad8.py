# Parse report from Rad-8 generated from R script

import scripts.parsers.baseparse as baseparse
import re

class Rad8Parse(baseparse.BaseParse):
    def __init__(self, file: str):
        super().__init__(file)

        if self.error_code is baseparse.ParseError.PARSE_OK:
            self.extract() 

    def extract(self):
        self._add_extract('RXR', r'(Hospital[\s]*number:)\s*(RXR(\d){7})', 2)
        self._add_extract('date', r'(Recording date:)[\s]*(\d{1,2}[\\/\.:]\d{1,2}[\\/\.:]\d{2,4})', 2)
        self._add_extract('dob', r'(Date of birth:)[\s]*(\d{1,2}[\\/\.:]\d{1,2}[\\/\.:]\d{2,4})', 2)

        self._add_extract('odi', r'(ODI)[\s]*(\d{1,3}\.?\d?)', 2)
        self._add_extract('hri', r'(HRI)[\s]*(\d{1,3}\.?\d?)', 2)

        re_name = re.compile(r'(Name:)[\s]*([A-Z][a-z]+)[\s]+([A-Z][a-z]+)')
        result = re_name.search(self.text)
        if result is None:
            self._log('No name extracted from {0}\n'.format(self.source_file))
        else:
            self.extracted['fname'] = result.group(2)
            self.extracted['lname'] = result.group(3)

        re_notes = re.compile(r'Notes:[\s]*([\s\S]+?(?=Report:))').search(self.text)
        re_report = re.compile(r'Report:[\s]*([\s\S]+?(?=\n\nSummary))').search(self.text)

        if re_notes is None:
            if re_report is None:
                self._log('No notes or report extracted from {0}\n'.format(self.source_file))
            else:
                self.extracted['report'] = re_report.search(self.text).group(1)
        
        else:
            if re_report is None:
                self.extracted['report'] = 'Notes:\n' + re_notes.group(1).rstrip()
            else:
                self.extracted['report'] = 'Notes:\n' + re_notes.group(1).rstrip() + \
                    '\n\nReport:\n' + re_report.group(1)


