from models.users.users import User
from config.config import sensitive_level_3

class Nurse(User):
    '''
    Nurse class inherit User class.
    '''
    def __init__(self, username, password):
        super().__init__(username, password)
        self.type = 'nurse'
        self.sensitive_level = sensitive_level_3
        

