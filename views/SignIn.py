from functions.config_file_reader import ConfigFileReader
from .UIFinder import UIFinder
from functions.auth_hash_helper import AuthHelper

class SignInPage:
    
    @staticmethod
    def show():
        ini_msg = "Enter username and password to login\nenter exit to go back\n"
        user_input_username = ''
        user_input_password = ''
        while True:
            user_input_username = input("Enter Your username:- ").strip()
            if(user_input_password == 'exit' or user_input_username == 'exit'):
                return -1
            user_input_password = input("Enter Your password:- ").strip()
            if(user_input_password == 'exit' or user_input_username == 'exit'):
                return -1
            user_record = ConfigFileReader.find_by_username_and_password(user_input_username,AuthHelper.hashed_password(user_input_password))
            if(user_record ==False):
                print("Invalid username or password\npress 1 to signup\npress enter to try again")
                input()
            else:
                # ConfigFileReader.print_rec(user_record)
                return UIFinder.showUI(user_record)
                break
        
    