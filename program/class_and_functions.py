import random
import json
from crypto import Criptography
from crypto import transform_hash

def init_cryptography():
    global cryptography
    cryptography = Criptography()
    try:
        with open("secret.key", "x") as key_file:
            cryptography.define_key()
    except FileExistsError:
        cryptography.remember_key()
    return cryptography

def line():
    """
    Displays a separator line.
    """
    print('—' * 80)

def menu():
    """
    Displays the main menu with available options.
    """
    line()
    print("1 - Access your passwords")
    print("2 - Create new passwords for new accounts")
    print("3 - Search for a specific password")
    print("4 - Finish program")
    line()

def show_logins():
    """
    Displays all accounts created by the user,
    including the username, password, and platform.
    """
    with open('data_passwords.txt', 'r') as archive:
        lines = archive.readlines()
        line()
        for c in range(3, len(lines)):
            print(cryptography.decrypt(lines[c].strip()))
        line()

def search_password():
    """
    Searches for a specific account and displays the username and password.
    """
    with open('data_passwords.txt', 'r') as archive:
        lines = archive.readlines()
        account_source = str(input('Enter the account platform so I can search for it: ')).strip()
        find = ''
        line()
        for c in range(3, len(lines)):
            user_password = cryptography.decrypt(lines[c].strip())
            user_password = user_password.split()
            if user_password[1] == account_source:
                find = user_password
                print(f"This account uses the username: \033[34m{find[0]}\033[m and the password: \033[32m{find[2]}\033[m")
        if find == '':
            print("\033[31mAccount not found.\033[m") 
        line()

def create_database(name_archive):
    with open(name_archive, "x") as archive:
        data = {
                "user_data": {
                                "username": "",
                                "master_key": ""
                                                    },
                "accounts": []
                }
        json.dump(data, archive, indent=4)













def generate_password():
        """
        Generates a secure password for the user.
        """
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
        password = ''.join(random.choice(characters) for i in range(12))
        return password

def security_check(key_access, color):
    """
    Checks whether the user knows the access key before allowing access to passwords.
    """
    key = input('Enter your access key: ').strip()
    if transform_hash(key) == key_access:
        return True
    else:
        print(f'{color}WRONG KEY!!! The program will now close.')
        return False


class User:
    def __init__(self, name, login_place):
        # attributes
        self.username = name
        self.login_place = login_place
        self.password = generate_password()
    
    # methods
    def new_login(self):
        """
        Registers a new account and generates a password for it.
        """
        with open('data_passwords.txt', 'a') as archive:
            data = f"{self.username:<30}{self.login_place:^20}{self.password:>20}"
            archive.write(cryptography.encrypt(data) + "\n")