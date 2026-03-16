from cryptography.fernet import Fernet
import hashlib


def transform_hash(data):
    data = hashlib.sha224(data.encode())
    return data.hexdigest()
    

class Criptography:
    def __init__(self):
        # attributes
        self.key_crypto = None

    # methods
    def define_key(self):
        """
        Generate the master key to encrypt and decrypt risks informations
        """
        self.key_crypto = Fernet.generate_key()
        with open("secret.key", "wb") as key_file:
            key_file.write(self.key_crypto)

    def remember_key(self):
        """
        Remember the key and input on the class attribute
        """
        with open("secret.key", "rb") as key_file:
            self.key_crypto = key_file.readline().strip()

    def encrypt(self, data):
        """
        encrypt and write all the user's data informed
        """
        f = Fernet(self.key_crypto)
        if isinstance(data, list):
            encrypted_info = []
            for c in data:
                encrypted_info.append(f.encrypt(c.encode()).decode)
            return encrypted_info
        else:
            return f.encrypt(data.encode()).decode()

    def decrypt(self, data):
        """
        decrypt and return the selected data for the user
        """
        f = Fernet(self.key_crypto)
        decrypted_info = f.decrypt(data).decode()
        return decrypted_info
