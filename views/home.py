from .SignIn import SignInPage

class HomePage:

    def __init__(self):
        ini_msg = "Welcome to the system.\nPress 1 to login to the system\nPress 2 to exit\n"
        while True:
            print(ini_msg)
            user_input = input("Enter your selection:- ").strip()

            if user_input == "1":
                re = SignInPage.show()
                if(re == -1):
                    continue
                print("............Terminated...............\n")
                break
            elif user_input == "2":
                print("............Terminated...............\n")
                break
            else:
                print("Invalid input\n")
                