from .add_n_view_user_records import AddViewUsers
from views.UserUi.add_n_view_records import AddViewRecords


class PatientUI:
    
    @staticmethod
    def showUI(username):
        ini_msg = "welcome "+username+" .\n press 1 to view your details\npress 2 to view your lab test records.\n press 3 to view your drug prescription records\n press 4 to view your sickness detils\npress 5 to logout"
        while(True):
            print(ini_msg)
            inp = input().strip()
            if(inp == '1'):
                val = AddViewUsers.findowndetails(username)
                print("===============================================================================")
            elif(inp == '2'):
                val = AddViewRecords.find_own_records(username,'lab record')
                print("===============================================================================")
            elif(inp == '3'):
                val = AddViewRecords.find_own_records(username,'sickness record')
                print("===============================================================================")
            elif(inp == '4'):
                val = AddViewRecords.find_own_records(username,'drug record')
                print("===============================================================================")
            elif(inp == '5'):
                print("===============================================================================")
                return -1