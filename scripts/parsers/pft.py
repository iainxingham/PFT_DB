# Parser for full PFT report

import scripts.parsers.baseparse as baseparse
import re

class PFTParse(baseparse.BaseParse):
    def __init__(self, file: str):
        super().__init__(file)

        if self.error_code is baseparse.ParseError.PARSE_OK:
            self.extract() 

    def extract(self):
        self._add_extract('RXR', r'Patient ID:[\s]*(((rxr)|(RXR))(\d){7})', 1)
        self._add_extract('date', r'Study Date:[\s]*(\d{1,2}[\\/\.:]\d{1,2}[\\/\.:]\d{2,4})', 1)
        self._add_extract('dob', r'Birth Date:[\s]*(\d{1,2}[\\/\.:]\d{1,2}[\\/\.:]\d{2,4})', 1)

        self._add_extract('height', r'Height: (\d{2,3}(\.\d)?) cm', 1)
        self._add_extract('weight', r'Weight: (\d{2,3}(\.\d)?) kg', 1)

        self._add_extract('lname', r'Last Name:[\s]*([A-Za-z]+)', 1)
        self._add_extract('fname', r'First Name:[\s]*([A-Za-z]+)', 1)

        lung_func = {'FEV1': r'FEV1.*',
                     'FVC': r'FVC.*',
                     'TLco': r'TLco.*',
                     'VAsb': r'VAsb.*',
                     'KCO': r'KCO.*',
                     'FRC': r'FRC.*',
                     'VC': r'(?<!F)VC.*',
                     'TLC': r'TLC.*',
                     'RV': r'RV .*',
                     'RV_TLC': r'RV/TLC.*'
                     }

        for i in lung_func:
            self.extracted[i] = self.extract_lung_func(lung_func[i], i)

    def extract_lung_func(self, regex: str, measurement: str) -> dict:
        re_lung = re.compile(regex)
        re_values = re.compile(r'(-?\d{1,3}\.?\d{0,2})')

        if measurement == 'FEV1':
            vals = re_values.findall(re_lung.search(self.text).group(0))[1:]
        elif measurement == 'VC':
            vals = re_values.findall(re_lung.findall(self.text)[1])
        else:
            vals = re_values.findall(re_lung.search(self.text).group(0))
        
        if len(vals) == 4:
            return {'Predicted': float(vals[0]),
                    'Measured': float(vals[1]),
                    'Percent_pred': float(vals[2]),
                    'SR': float(vals[3])}
        elif len(vals) == 3:
            return {'Predicted': float(vals[0]),
                    'Measured': float(vals[1]),
                    'Percent_pred': float(vals[2])}
        elif len(vals) == 8:
            return {'Predicted': float(vals[0]),
                    'Measured_pre': float(vals[1]),
                    'Percent_pred_pre': float(vals[2]),
                    'Measured_post': float(vals[3]),
                    'Percent_pred_post': float(vals[4]),
                    'Percent_change': float(vals[5]),
                    'SR_pre': float(vals[6]),
                    'SR_post': float(vals[7])}
        else:
            self._log('Couldn\'t extract {0} from {1}'.format(measurement, self.source_file))
            return {}
