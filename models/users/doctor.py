from models.users.users import User
from config.config import sensitive_level_2

class Doctor(User):
    '''
    Doctor class inherit User class.
    '''
    def __init__(self, username, password):
        super().__init__(username, password)
        self.type = 'doctor'
        self.sensitive_level = sensitive_level_2

