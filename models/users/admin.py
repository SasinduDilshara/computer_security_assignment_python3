from models.users.users import User
from config.config import sensitive_level_1

class Admin(User):
    '''
    Admin class inherit User class.
    '''
    def __init__(self, username, password):
        super().__init__(username, password)
        self.type = 'admin'
        self.sensitive_level = sensitive_level_1
        

