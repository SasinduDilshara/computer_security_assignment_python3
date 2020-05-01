import hashlib
from config.config import salt_to_hash

class AuthHelper:

    @staticmethod
    def hashed_password(password):
        '''
        This method hashed the password based on md5 algorithm
        '''
        try:
            salt = salt_to_hash
            passstring = salt.encode('utf-8') + password.encode('utf-8')
            hashed = hashlib.md5(passstring).hexdigest()

            return hashed
        except Exception as e:
            print("Error occur in hashing")
            print(e)
            return False