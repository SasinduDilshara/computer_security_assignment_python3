import pickle
from functions.file_reader import FileReader
from functions.config_file_reader import ConfigFileReader
from config.config import record_file
import os

class DataFileReader:
    # filename = "../database/"+config_file
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "../ztest/record_file"
    filename = os.path.join(script_dir, rel_path)
    
    @staticmethod
    def find_by_username(username_):
        '''
        find_by_attribute(username)
        This method find any data record contain in file filter by username
        '''
        try:
            records = FileReader.loadall(DataFileReader.filename)
            for record in records:
                if(record.username == username_):
                    return record
                    break
            else:
                return False
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
                recs = FileReader.loadall(DataFileReader.filename)
                for rec in recs:
                    user = DataFileReader.get_user_by_username(rec.username)
                    if(user == False):
                        return False
                    else:
                        if(user.type in type_):
                            load[user.type].append(rec)
                return load
        except Exception as e:
            print("Error happen in loadall")
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

            
