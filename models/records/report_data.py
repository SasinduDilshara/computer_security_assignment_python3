from abc import ABC

class ReportData(ABC):
    '''
    Abstract class for ReportData.
    '''
    def __init__(self,patient_username, sensitivity_level,description,date):
        self.username = patient_username
        self.__sensitivity_level = sensitivity_level
        self.date = date
        self.description = description

    def getSensivity(self):
        return self.__sensitivity_level
    def setSensivity(self,sensitivity_level):
        self.__sensitivity_level = sensitivity_level
        

