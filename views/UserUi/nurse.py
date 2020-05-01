class NurseUI:
    
    @staticmethod
    def showUI(username):
        ini_msg = "welcome "+username+" .\n press 1 to view patients records\npress 2 to view lab test records.\n press 3 to view drug prescription records\n press 4 to view sickness detils\npress 5 to logout"
        ini_msg = ini_msg+"\nAll the records show according to some priviledges"
        while(True):
            print(ini_msg)
            inp = input().strip()
            if(inp == '1'):
                pass
            elif(inp == '2'):
                pass
            elif(inp == '3'):
                pass
            elif(inp == '4'):
                pass
            elif(inp == '5'):
                return -1