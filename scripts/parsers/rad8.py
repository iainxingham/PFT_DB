# Parse report from Rad-8 generated from R script

import baseparse
import re

class Rad8Parse(baseparse.BaseParse):
    def __init__(self, file: str):
        super().__init__(self, file)

    def extract(self):
        re_rxr = re.compile(r'(Hospital[\s]*number:)\s*(RXR(\d){7})')
        self.extracted['RXR'] = re_rxr.search(self.text).group(2)
        re_name = re.compile(r'(Name:)[\s]*([A-Z][a-z]+)[\s]+([A-Z][a-z]+)')
        self.extracted['fname'] = re_name.search(self.text).group(2)
        self.extracted['lname'] = re_name.search(self.text).group(3)
        re_notes = re.compile(r'Notes:[\s]*([\s\S]+?(?=Report:))')
        self.extracted['notes'] = re_notes.search(self.text).group(1).rstrip()
        re_report = re.compile(r'Report:[\s]*([\s\S]+?(?=\n\nSummary))')
        self.extracted['report'] = re_report.search(self.text).group(1) # Combine with notes?
        re_dob = re.compile(r'(Date of birth:)[\s]*(\d{1,2}[\\/\.:]\d{1,2}[\\/\.:]\d{2,4})')
        self.extracted['dob'] = re_dob.search(self.text).group(2)
        re_odi = re.compile(r'(ODI)[\s]*(\d{1,3}\.?\d?)')
        self.extracted['odi'] = re_odi.search(self.text).group(2)
        re_hri = re.compile(r'(HRI)[\s]*(\d{1,3}\.?\d?)')
        self.extracted['hri'] = re_hri.search(self.text).group(2)
        re_date = re.compile(r'(Recording date:)[\s]*(\d{1,2}[\\/\.:]\d{1,2}[\\/\.:]\d{2,4})')
        self.extracted['date'] = re_date.search(self.text).group(2)

