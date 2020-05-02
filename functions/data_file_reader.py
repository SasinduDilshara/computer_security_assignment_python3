import pickle
from functions.file_reader import FileReader
from functions.config_file_reader import ConfigFileReader
from config.config import record_file
from config.config import sensitive_level_1,sensitive_level_2,sensitive_level_3,sensitive_level_4
from models.personal_data.personal_data_parent import PersonalData
from models.records.report_data import ReportData
from models.records.lab_test_prescription import LabTestPrescription
from models.records.drug_prescription import DrugPrescription
from models.records.sickness_details import SicknessDetails
import os

class DataFileReader:
    # filename = "../database/"+config_file
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "../db/record_file"
    filename = os.path.join(script_dir, rel_path)
    
    @staticmethod
    def find_by_username(username_):
        '''
        find_by_attribute(username)
        This method find any data record contain in file filter by username
        '''
        try:
            recs = []
            records = FileReader.loadall(DataFileReader.filename)
            for record in records:
                if(record.username == username_):
                    recs.append(record)
            return recs
            
        except Exception as e:
            print("Error happen in find_by_username")
            print(e)
            return False

    @staticmethod
    def get_user_by_username(username):
        rec = ConfigFileReader.find_by_username(username)
        if(rec == False):
            return False
        else:
            return rec
            

    @staticmethod
    def loadall(type_=''):
        '''
        loadall(type) ~type is a list containing admin,doctor,patient,nurse)
        This method return all the data conatined in recordfile under type condition
        '''
        load = {'nurse':[],'doctor':[],'patient':[]}
        try:
            if(type_ == ''):
                return FileReader.loadall(DataFileReader.filename)
            else:
                recss= []
                recs = FileReader.loadall(DataFileReader.filename)
                try:
                    for rec in recs:
                        if(isinstance(rec,PersonalData)):
                            recss.append(rec)
                except Exception:
                    recss.append([recs])
                for rec in recss:
                    user = DataFileReader.get_user_by_username(rec.username)
                    if(user == False):
                        return False
                    else:
                        if(user.type in type_):
                            load[user.type].append(rec)
                return load
        except Exception as e:
            print("No data to view")
            print(e)
            return False

    @staticmethod
    def add(obj):
        '''
        add(object)
        This method add new detail to config file
        '''
        try:
            return FileReader.add(DataFileReader.filename, obj)
        except Exception as e:
            print("Error happen in add")
            print(e)
            return False
    @staticmethod 
    def print_rec(records=False):
        '''
        print all given user records
        default print all
        '''
        try:
            if(records == False):
                records = FileReader.loadall(DataFileReader.filename)
            try:
                for record in records:
                    print(record.username)
            except Exception as ee:
                print(records.username)
        except Exception as e:
            print("Error happen in printrec")
            print(e)
            return False

    @staticmethod
    def loadRecods(type_=''):
        '''
        type = labreport,drug_prscription,sickness_detail\n
        Default value for type = '' which gives the all records
        '''
        try:
            recss =  FileReader.loadall(DataFileReader.filename)
            recs = []
            if(type_ == ''):
                for rec in recss:
                    if(isinstance(rec,ReportData)):
                        recs.append(rec)
                return recs
            else:
                if(type_ == 'lab record'):
                    for rec in recss:
                        if(isinstance(rec,LabTestPrescription)):
                            recs.append(rec)
                    return recs
                elif(type_ == 'sickness record'):
                    for rec in recss:
                        if(isinstance(rec,SicknessDetails)):
                            recs.append(rec)
                    return recs
                elif(type_ == 'drug record'):
                    for rec in recss:
                        if(isinstance(rec,DrugPrescription)):
                            recs.append(rec)
                    return recs
                else:
                    print("no Report")
                    return False
        except Exception as e:
            print("No record to get")
            print(e)
            return False

    @staticmethod
    def Record_find_by_username(username,type_,sl = sensitive_level_4):
        records = DataFileReader.loadRecods(type_)
        if(records == False):
            print("No record for "+username+".")
            return False
        else:
            recc= [] 
            for rec in records:
                if(int(rec.getSensivity()) >= int(sl) and rec.username == username):
                    recc.append(rec)
            return recc

    @staticmethod
    def Record_find_by_finder_username(username,type_):
        '''
        '''
        finder = DataFileReader.get_user_by_username(username)
        if(finder == False):
            print("No records .")
            return False
        records = DataFileReader.loadRecods(type_)
        if(records == False):
            print("No records .")
            return False
        else:
            try:
                recc= [] 
                for rec in records:
                    if(int(rec.getSensivity()) >= int(finder.sensitive_level)):
                        recc.append(rec)
                return recc
            except Exception as e:
                print("\n Something went wrong about sensitivity\nTry again")
                print(e)
                return False
            
