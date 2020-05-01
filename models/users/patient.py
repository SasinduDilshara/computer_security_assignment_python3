from models.users.users import User


class Patient(User):
    '''
    Patient class inherit User class.
    '''
    def __init__(self, username, password):
        super().__init__(username, password)
        

