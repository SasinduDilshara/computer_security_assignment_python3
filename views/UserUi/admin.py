from views.UserUi.add_n_view_user_records import AddViewUsers
from views.UserUi.add_n_view_records import AddViewRecords

class AdminUI:
    
    @staticmethod
    def showUI(username):
        ini_msg = "welcome "+username+" .\n press 1 to view and add user records\npress 2 to view lab test records.\n press 3 to view drug prescription records\n press 4 to view sickness detils\npress 5 to logout"
        while(True):
            print(ini_msg)
            inp = input().strip()
            if(inp == '1'):
                val = AddViewUsers.addMembers(username)
                print("\n")
                # break
            elif(inp == '2'):
                val = AddViewRecords.viewRecords(username,'lab record')
            elif(inp == '3'):
                val = AddViewRecords.viewRecords(username,'sickness record')
            elif(inp == '4'):
                val = AddViewRecords.viewRecords(username,'drug report')
            elif(inp == '5'):
                return -1