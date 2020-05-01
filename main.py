from functions.file_reader import FileReader
from models.users.admin import Admin
from models.users.doctor import Doctor
from models.users.nurse import Nurse
from models.users.patient import Patient
from functions.config_file_reader import ConfigFileReader
from views.home import HomePage  

def main():
    # ConfigFileReader.add(Admin("admin","admin"))
    # ConfigFileReader.add(Doctor("doctor","doctor"))
    # ConfigFileReader.add(Nurse("nurse","nurse"))
    # ConfigFileReader.add(Patient("patient","patient"))
    # ConfigFileReader.add(Admin("admin1","admin1"))
    # for i in ConfigFileReader.loadall():
    #     print(i.username,i.getPassword(),i.sensitive_level,i.type)
    # a = ConfigFileReader.print_rec()
    # if(a!=False):
    #     print(a.username,a.getPassword())
    # else:
    #     print(a)
    HomePage()

if __name__ == '__main__':
    main()

