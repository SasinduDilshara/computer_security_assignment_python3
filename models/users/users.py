from abc import ABC
from functions.auth_hash_helper import AuthHelper

class User(ABC):
    '''
    Abstract class for users.
    '''
    def __init__(self,username, password):
        self.username = username
        self.__password = AuthHelper.hashed_password(password)

    def getPassword(self):
        return self.__password
    def setPassword(self,password):
        self.__password = AuthHelper.hashed_password(password)
        

