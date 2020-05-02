
from .add_n_view_user_records import AddViewUsers
from views.UserUi.add_n_view_records import AddViewRecords

class NurseUI:
    
    @staticmethod
    def showUI(username):
        ini_msg = "welcome "+username+" .\n press 1 to view and add patients records\npress 2 to view lab test records.\n press 3 to view sickness prescription records\n press 4 to view drug detils\npress 5 to view a specific user record\npress 6 to view your profile\npress 7 to change the password\npress 8 to logout"
        ini_msg = ini_msg+"\nAll the records show according to some priviledges"
        while(True):
            print(ini_msg)
            inp = input().strip()
            if(inp == '1'):
                val = AddViewUsers.addMembers(username)
                print("================================================================================================")
                print("\n")
            elif(inp == '2'):
                val = AddViewRecords.viewRecords(username,'lab record')
                print("================================================================================================")
            elif(inp == '3'):
                val = AddViewRecords.viewRecords(username,'sickness record')
                print("================================================================================================")
            elif(inp == '4'):
                val = AddViewRecords.viewRecords(username,'drug record')
                print("================================================================================================")                
            elif(inp == '5'):
                val = AddViewRecords.find_user_records(username)
            elif(inp == '6'):
                val = AddViewUsers.findowndetails(username)
                print("================================================================================================")
            elif(inp == '7'):
                val = AddViewUsers.changepassword(username)
                print("===============================================================================")
            elif(inp == '8'):
                print("================================================================================================")
                return -1