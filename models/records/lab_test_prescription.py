
from models.records.report_data import ReportData

class LabTestPrescription(ReportData):
    '''
    LabTestPrescription class inherit ReportData class.
    __init__(self, patient_username,result, sensitivity_level,description,date)
    Create one object for each prescription
    '''
    def __init__(self, patient_username,result, sensitivity_level,description,date):
        super().__init__(patient_username, sensitivity_level,description,date)
        self.result = result

