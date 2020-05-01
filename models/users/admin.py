from models.users.users import User


class Admin(User):
    '''
    Admin class inherit User class.
    '''
    def __init__(self, username, password):
        super().__init__(username, password)
        

