

from models.records.report_data import ReportData

class SicknessDetails(ReportData):
    '''
    SicknessDetails class inherit ReportData class.
    __init__(self, patient_username,result, sensitivity_level,description,date)
    Create one object for each sickness
    '''
    def __init__(self, patient_username,sickness_name, sensitivity_level,description,date):
        super().__init__(patient_username, sensitivity_level,date)
        self.sickness_name = sickness_name

