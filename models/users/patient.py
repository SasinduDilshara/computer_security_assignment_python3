from models.users.users import User
from config.config import sensitive_level_4

class Patient(User):
    '''
    Patient class inherit User class.
    '''
    def __init__(self, username, password):
        super().__init__(username, password)
        self.type = 'patient'
        self.sensitive_level = sensitive_level_4

