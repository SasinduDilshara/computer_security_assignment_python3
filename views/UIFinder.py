from .UserUi.admin import AdminUI
from .UserUi.doctor import DoctorUI
from .UserUi.nurse import NurseUI
from .UserUi.patient import PatientUI
from models.users.admin import Admin
from models.users.doctor import Doctor
from models.users.nurse import Nurse
from models.users.patient import Patient

class UIFinder:

    @staticmethod
    def showUI(record):
        try:
            if(isinstance(record,Admin)):
                return AdminUI.showUI(record.username)
            elif(isinstance(record,Doctor)):
                return DoctorUI.showUI(record.username)
            elif(isinstance(record,Nurse)):
                return NurseUI.showUI(record.username)
            elif(isinstance(record,Patient)):
                return PatientUI.showUI(record.username)
            else:
                print("Something get wrong. User interface can't be find. Try again")
        except Exception as e:
            print("Something get wrong. User interface can't be find. Try again")
            print(e)
            print("\n")