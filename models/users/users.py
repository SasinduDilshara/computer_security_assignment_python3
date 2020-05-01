from abc import ABC

class User(ABC):
    '''
    Abstract class for users.
    '''
    def __init__(self, username, password):
        self.username = username
        self.password = password
        

