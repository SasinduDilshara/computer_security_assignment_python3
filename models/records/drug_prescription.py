
from models.records.report_data import ReportData

class DrugPrescription(ReportData):
    '''
    DrugPrescription class inherit ReportData class.
    __init__(self, patient_username,valid_period, sensitivity_level,description,date)
    Create one object for each prescription
    '''
    def __init__(self, patient_username,valid_period, sensitivity_level,description,date):
        super().__init__(patient_username, sensitivity_level,description,date)
        self.valid_period = valid_period

