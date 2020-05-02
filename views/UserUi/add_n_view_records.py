from functions.config_file_reader import ConfigFileReader
from functions.data_file_reader import DataFileReader
from models.users.doctor import Doctor
from models.users.nurse import Nurse
from models.users.patient import Patient
from models.personal_data.patient_personal_details import PatientData
from models.personal_data.doctor_personal_details import DoctorData
from models.personal_data.nurse_personal_details import NurseData
from models.records.report_data import ReportData
from models.records.lab_test_prescription import LabTestPrescription
from models.records.drug_prescription import DrugPrescription
from models.records.sickness_details import SicknessDetails
from config.config import sensitive_level_1,sensitive_level_2,sensitive_level_3,sensitive_level_4
import datetime



class AddViewRecords:
 
    @staticmethod
    def find_user_records(username):
        '''
        find all records for a specific user.
        find_user_records(seracher,owner)
        '''
        try:
            while True:
                print("Enter the type of your report ex:- lab record | sickness record | drug record\n Other inputs will discarded")
                print("Type 'exit' to exit.")
                type_ = input("Enter the type:- ").strip()
                if(type_ == 'exit'):
                    return -1
                if(type_ not in ['lab record' , 'sickness record' , 'drug record']):
                    print("\nInvalid type . Type Again\n")
                    continue
                else:
                    break
            while True:
                patient = input("Enter the patient username:- ").strip()
                find = ConfigFileReader.find_by_username(patient)
                if(patient == 'exit'):
                    return -1
                if(find == False or find.type != 'patient'):
                    print("\nUsername can't find . Type Again\n")
                    continue
                else:
                    break
            recs = DataFileReader.Record_find_by_finder_username(username,type_)
            records = []
            for i in recs:
                if(i.username == patient):
                    records.append(i)
            if(records == False):
                return False
            else:
                l = []
                d = []
                s =[]
                for r in records:
                    if(isinstance(r,LabTestPrescription)):
                        l.append(r)
                    elif(isinstance(r,SicknessDetails)):
                        s.append(r)
                    elif(isinstance(r,DrugPrescription)):
                        d.append(r)
                if(len(l) != 0):
                    print("\nLab Descriptions\n")
                    for i in l:
                        print("patient username: "+i.username)
                        print("Description: "+i.description) 
                        print("Result: "+i.result) 
                        print("Issued Date: "+i.date.__str__())
                        print("\n")
                if(len(d) != 0):
                    print("\nDrug Descriptions\n")
                    for i in d:
                        print("patient username: "+i.username)
                        print("Description: "+i.description) 
                        print("valid_period: "+i.valid_period) 
                        print("Issued Date: "+i.date.__str__())
                        print("\n")
                if(len(s) != 0):
                    print("\nSickness Descriptions\n")
                    for i in s:
                        print("patient username: "+i.username)
                        print("Description: "+i.description) 
                        print("sickness_name: "+i.sickness_name) 
                        print("Issued Date: "+i.date.__str__())
                        print("\n") 
                    
        except Exception as e:
            print("No record\n")
            print(e)
            return False

    @staticmethod
    def viewRecords(username,type_ = ''):
        '''
        Type can be either report type or all(given by '')
        '''
        records = DataFileReader.Record_find_by_finder_username(username,type_)
        if(records == False):
            print("No records\n")
            return False
        else:
            l = []
            d = []
            s =[]
            for r in records:
                if(isinstance(r,LabTestPrescription)):
                    l.append(r)
                elif(isinstance(r,SicknessDetails)):
                    s.append(r)
                elif(isinstance(r,DrugPrescription)):
                    d.append(r)
            if(len(l) != 0):
                print("\nLab Descriptions\n")
                for i in l:
                    print("patient username: "+i.username)
                    print("Description: "+i.description) 
                    print("Result: "+i.result) 
                    print("Issued Date: "+i.date.__str__())
                    print("\n")
            if(len(d) != 0):
                print("\nDrug Descriptions\n")
                for i in d:
                    print("patient username: "+i.username)
                    print("Description: "+i.description) 
                    print("valid_period: "+i.valid_period) 
                    print("Issued Date: "+i.date.__str__())
                    print("\n")
            if(len(s) != 0):
                print("\nSickness Descriptions\n")
                for i in s:
                    print("patient username: "+i.username)
                    print("Description: "+i.description) 
                    print("sickness_name: "+i.sickness_name) 
                    print("Issued Date: "+i.date.__str__())
                    print("\n") 
    @staticmethod
    def addRecords(username):
        user_ = ConfigFileReader.find_by_username(username)
        if(user_ == False or user_.type not in ['doctor','admin']):
            print("You haven't access to add records.\n")
        else:
            while True:
                print("Enter the type of your report ex:- lab report | sickness report | drug report\n Other inputs will discarded")
                print("Type 'exit' to exit.")
                type_ = input("Enter the type:- ").strip()
                if(type_ == 'exit'):
                    return -1
                if(type_ not in ['lab report' , 'sickness report' , 'drug report']):
                    print("\nInvalid type . Type Again\n")
                    continue
                else:
                    break
            while True:
                patient = input("Enter the patient username:- ").strip()
                find = ConfigFileReader.find_by_username(patient)
                if(patient == 'exit'):
                    return -1
                if(find == False or find.type != 'patient'):
                    print("\nUsername can't find . Type Again\n")
                    continue
                else:
                    break
            while True:
                print("\nType the sensivity. sensivity value should be one of below values")
                print("\t"+sensitive_level_1+","+sensitive_level_2+","+sensitive_level_3+","+sensitive_level_4)
                sen = input("Enter the sensivty of the record:- ")
                if(sen == 'exit'):
                    return -1
                if(sen not in [sensitive_level_1,sensitive_level_2,sensitive_level_3,sensitive_level_4]):
                    print("\nInvalid value. Try again\n")
                    continue
                else:
                    break
            description = input("Enter the description:- ").strip()
            if(description == 'exit'):
                return -1
            date = datetime.date.today()
            if(type_ == 'lab report'):
                result = input("Enter the result(If result not came yet press enter) :- ")
                if(result == 'exit'):
                    return -1
                if(result ==''):
                    result = 'Pending'
                obj = LabTestPrescription(patient,result,sen,description,date)
                
            elif(type_ == 'sickness report'):
                name = input("Enter the sickness name :- ")
                if(name == 'exit'):
                    return -1
                obj = SicknessDetails(patient,name,sen,description,date)
                
            elif(type_ == 'drug report'):
                valid_period = input("Enter the valid period :- ")
                if(valid_period == 'exit'):
                    return -1
                obj = DrugPrescription(patient,valid_period,sen,description,date)
                
            else:
                print("\nwrong type. Try again\n")
        if(obj == None or obj ==False):
            print("\nwrong type. Try again\n")
            return False
        else:
            result = DataFileReader.add(obj)
            if(result == False):
                return False
            else:
                print("Succefully added")
                return True
            




                           