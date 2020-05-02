from functions.config_file_reader import ConfigFileReader
from functions.data_file_reader import DataFileReader
from models.users.doctor import Doctor
from models.users.nurse import Nurse
from models.users.patient import Patient
from models.personal_data.patient_personal_details import PatientData
from models.personal_data.doctor_personal_details import DoctorData
from models.personal_data.nurse_personal_details import NurseData

class AddViewUsers:

    @staticmethod
    def viewMembers(username):
        try:
            user_ = ConfigFileReader.find_by_username(username)
            if(user_ == False):
                return -1
            else:
                if(user_.type == 'admin'):
                    recs = DataFileReader.loadall(['doctor','nurse','patient'])
                    # print(recs)
                    for k in recs:
                        print(k+"\n")
                        for ele in recs[k]:
                            print("\n")
                            print(ele.__str__())
                    return 1
                elif(user_.type == 'doctor'):
                    recs = DataFileReader.loadall(['nurse','patient'])
                    for k in recs:
                        print(k+"\n")
                        for ele in recs[k]:
                            print("\n")
                            print(ele.__str__())
                    return 1
                elif(user_.type == 'nurse'):
                    recs = DataFileReader.loadall(['patient'])
                    for k in recs:
                        print(k+"\n")
                        for ele in recs[k]:
                            print("\n")
                            print(ele.__str__())
                    return 1
                else:
                    print("you haven't priviledges")
                    return -1
                return 1
        except Exception as e:
            print("error in view members")
            print(e)
            return -1

    @staticmethod
    def addMembers(username):
        try:
            user_ = ConfigFileReader.find_by_username(username)
            if(user_ == False):
                return -1
            else:
                if(user_.type == 'admin'):
                    val = AddViewUsers.adminAdd(username)
                elif(user_.type == 'doctor'):
                    val = AddViewUsers.doctorAdd(username)
                elif(user_.type == 'nurse'):
                    val = AddViewUsers.nurseAdd(username)
                else:
                    print("Uou havent priviledges")
                    return -1
        except Exception as e:
            print("error in adding members")
            print(e)
            return -1
    
    @staticmethod
    def adminAdd(username):
        while True:
            print("\ntype 0 to view users\ntype 1 to add doctor\n type 2 to add nurse\ntype 3 to add patient\ntype 9 to exit")
            inp = input()
            if(inp == '0'):
                val = AddViewUsers.viewMembers(username)
                # return val
            elif(inp == '3'):
                val = AddViewUsers.patientCreate()
                # if(val == 'y'):
                #     continue
                # else:
                #     break
            elif(inp == '2'):
                val = AddViewUsers.nurseCreate()
                # if(val == 'y'):
                #     continue
                # else:
                #     break
            elif(inp == '1'):
                val = AddViewUsers.doctorCreate()
                # if(val == 'y'):
                #     continue
                # else:
                #     break
            elif(inp == '9'):
                return 1
            else:
                print("invalid input\n")


    @staticmethod
    def doctorAdd(username):
         while True:
            print("\ntype 0 to view patents and nurses\ntype 1 to add nurse\ntype 2 to add patient\ntype 9 to exit")
            inp = input()
            if(inp == '0'):
                val = AddViewUsers.viewMembers(username)
                # return val
            elif(inp == '2'):
                val = AddViewUsers.patientCreate()
                # if(val == 'y'):
                #     continue
                # else:
                #     break
            elif(inp == '1'):
                val = AddViewUsers.nurseCreate()
                # if(val == 'y'):
                #     continue
                # else:
                #     break
            elif(inp == '9'):
                return 1
            else:
                print("invalid input\n")
        
    @staticmethod
    def nurseAdd(username):
        while True:
            print("\ntype 0 to view patient details\ntype 1 to add patient\ntype 9 to exit")
            inp = input()
            if(inp == '0'):
                val = AddViewUsers.viewMembers(username)
                # return val
                # break
            if(inp == '1'):
                val = AddViewUsers.patientCreate()
                
                # if(val == 'y'):
                #     continue
                # else:
                #     break
            elif(inp == '9'):
                return 1
            else:
                print("invalid input\n") 


    @staticmethod
    def patientCreate():
        print("enter details")
        while True:
            username = input("Enter_username:- ")
            if(ConfigFileReader.find_by_username(username) != False):
                print("username exist. Type a new one\n")
                continue
            else:
                break
        firstName = input("Enter_firstName:- ")
        lastName = input("Enter_lastName:- ")  
        address = input("Enter_address:- ")
        while True:  
            telephone = input("Enter_telephone:- +94")
            try:
                int(telephone)
                if(len(telephone)<9):
                    print("enter a valid telephone number")
                    continue
                else:
                    break
                 
            except Exception:
                  print("enter a valid telephone number")
                  continue
        while True: 
            age = input("Enter_age:- ") 
            try:
                int(age)
                if(True):
                    break
            except Exception:
                  print("enter a valid age")
                  continue 
        special_notes = input("Enter_special_notes:- ")
        user_ = Patient(username,telephone) #initial password was phone number. Patient has to change it immediatly
        data_ = PatientData(username, firstName, lastName, telephone , address,age,special_notes)
        val1 =  ConfigFileReader.add(user_)
        val2 = DataFileReader.add(data_)

        if(val1 == False or val2 == False):  
            return False
        return True

    @staticmethod
    def doctorCreate():
        print("enter details")
        while True:
            username = input("Enter_username:- ")
            if(ConfigFileReader.find_by_username(username) != False):
                print("username exist. Type a new one\n")
                continue
            else:
                break
        firstName = input("Enter_firstName:- ")
        lastName = input("Enter_lastName:- ")  
        address = input("Enter_address:- ")
        while True:  
            telephone = input("Enter_telephone:- +94")
            try:
                int(telephone)
                if(len(telephone)<9):
                    print("enter a valid telephone number")
                    continue
                else:
                    break
                
            except Exception:
                print("enter a valid telephone number")
                continue
        nic = input("Enter_NIC:- ")
        doc_id = input("Enter_SLRC ID:- ")
        user_ = Doctor(username,telephone) #initial password was phone number. Patient has to change it immediatly
        data_ = DoctorData(username, firstName, lastName, telephone , address,doc_id,nic)
        val1 =  ConfigFileReader.add(user_)
        val2 = DataFileReader.add(data_)

        if(val1 == False or val2 == False):  
            return False
        return True


    @staticmethod
    def nurseCreate():
        print("enter details")
        while True:
            username = input("Enter_username:- ")
            if(ConfigFileReader.find_by_username(username) != False):
                print("username exist. Type a new one\n")
                continue
            else:
                break
        firstName = input("Enter_firstName:- ")
        lastName = input("Enter_lastName:- ")  
        address = input("Enter_address:- ")
        while True:  
            telephone = input("Enter_telephone:- +94")
            try:
                int(telephone)
                if(len(telephone)<9):
                    print("enter a valid telephone number")
                    continue
                else:
                    break
                
            except Exception:
                print("enter a valid telephone number")
                continue
        nic = input("Enter_NIC:- ")
        user_ = Nurse(username,telephone) #initial password was phone number. Patient has to change it immediatly
        data_ = NurseData(username, firstName, lastName, telephone , address,nic)
        val1 =  ConfigFileReader.add(user_)
        val2 = DataFileReader.add(data_)

        if(val1 == False or val2 == False):  
            return False
        return True