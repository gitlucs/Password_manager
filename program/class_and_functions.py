import secrets
import json
from crypto import Criptography
from crypto import transform_hash

data_base = "database.json"

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
    print("4 - Delete account")
    print("5 - recreate a password for an existing account")
    print("6 - Finish program")
    line()

def show_logins():
    """
    Displays all accounts created by the user,
    including the username, password, and platform.
    """
    data = read_data(data_base)
    line()
    print(f'{"username":<30}{"place":^20}{"password":^30}')
    for account in data["accounts"]:
        print(f'{account["username"]:<30}{account["place"]:^20}{cryptography.decrypt(account["password"]):^30}')
    line()

def search_password():
    """
    Searches for a specific account and displays the username and password.
    """
    data = read_data(data_base)
    account_source = str(input('Enter the account platform so I can search for it: ')).strip()
    find = 0
    line()
    for account in data["accounts"]:
        if account["place"] == account_source:
            find += 1
            print(f"This account uses the username: \033[34m{account["username"]}\033[m and the password: \033[32m{cryptography.decrypt(account['password'].strip())}\033[m")
    if find == 0:
        print("\033[31mAccount not found.\033[m") 
        line()

def create_database(name_archive):
    """
    creates a file which will have all the contents of user accounts and access
    """
    
    with open(name_archive, "x") as archive:
        data = {
                "user_data": {
                                "username": "",
                                "master_key": ""
                                                    },
                "accounts": []
                }
        json.dump(data, archive)
        

def read_data(name_archive):
    """
    read the data of archive
    """
    with open(name_archive, 'r') as archive:
        return json.load(archive)

def save_data(name_archive, data):
    """
    save the new data of archive
    """
    with open(name_archive,'w') as archive:
        json.dump(data, archive, indent = 4)




def generate_password():
        """
        Generates a secure password for the user.
        """
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
        password = ''.join(secrets.choice(characters) for i in range(12))
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
        data = read_data(data_base)
        new_login = {"username":self.username,"place": self.login_place, "password": cryptography.encrypt(self.password)}
        data["accounts"].append(new_login) 
        save_data(data_base, data)