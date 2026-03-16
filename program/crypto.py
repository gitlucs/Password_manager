from cryptography.fernet import Fernet
import hashlib
import base64



def transform_hash(data, salt, hex = False):
    salt = bytes.fromhex(salt)
    data = hashlib.pbkdf2_hmac("sha256", data, salt, 100000, 32)
    if hex == True:
        return data.hex()
    else:
        return data
    

class Criptography:
    def __init__(self):
        # attributes
        self.key_crypto = None

    # methods
    def define_key(self, data , salt):
        """
        Generate the master key to encrypt and decrypt risks informations
        """
        key = transform_hash(data, salt)
        self.key_crypto = base64.urlsafe_b64encode(key)
        return self.key_crypto


    def encrypt(self, data):
        """
        encrypt and write all the user's data informed
        """
        f = Fernet(self.key_crypto)
        return f.encrypt(data.encode()).decode()

    def decrypt(self, data):
        """
        decrypt and return the selected data for the user
        """
        f = Fernet(self.key_crypto)
        decrypted_info = f.decrypt(data.encode()).decode()
        return decrypted_info
