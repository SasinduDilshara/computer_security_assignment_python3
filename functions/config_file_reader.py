import pickle
from functions.file_reader import FileReader
from config.config import config_file
import os

class ConfigFileReader:
    # filename = "../database/"+config_file
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "../ztest/config_file"
    filename = os.path.join(script_dir, rel_path)
    
    @staticmethod
    def find_by_username(username_):
        '''
        find_by_attribute(username)
        This method find any data record contain in file filter by username
        '''
        try:
            records = FileReader.loadall(ConfigFileReader.filename)
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
    def find_by_username_and_password(username_,password__):
        '''
        find_by_attribute(username,password)
        This method find any data record contain in file filter by username amd password
        '''
        try:
            records = FileReader.loadall(ConfigFileReader.filename)
            for record in records:
                if(record.username == username_ and record.password == password__):
                    return record
                    break
            else:
                return False
        except Exception as e:
            print("Error happen in find_by_username_and_password")
            print(e)
            return False

    @staticmethod
    def loadall():
        '''
        loadall()
        This method return all the data conatined in configfile
        '''
        try:
            return FileReader.loadall(ConfigFileReader.filename)
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
            return FileReader.add(ConfigFileReader.filename, obj)
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
                records = FileReader.loadall(ConfigFileReader.filename)
            for record in records:
                print(record.username)
        except Exception as e:
            print("Error happen in loadall")
            print(e)
            return False   

            
