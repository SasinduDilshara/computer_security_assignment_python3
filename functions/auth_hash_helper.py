import hashlib
import config.config import salt_to_hash

class AuthHelper:

    @staticmethod
    def hashed_password(password):
        salt = salt_to_hash
        passstring = salt.encode('utf-8') + password.encode('utf-8')
        hashed = hashlib.md5(passtring).hexdigest()
        return hashed