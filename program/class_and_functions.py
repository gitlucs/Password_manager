import random
def line():
    """
    shows a line
    """
    print('—' * 80)

def menu():
    """
    show the main menu with options to user choice
    """
    line()
    print("1 - Access your passwords")
    print("2 - Create new passwords for new accounts")
    print("3 - Search for an specific password")
    print("4 - Finish program")
    line()

def show_logins():
    """
    show all accounts created by user
    including the username, password, and account source
    """
    with open('data_passwords.txt', 'r') as archive:
        lines = archive.readlines()
        line()
        for c in range(2, len(lines)):
            print(lines[c])
        line()

def search_password():
    """
    search an especific password and user, with the account source
    """
    with open('data_passwords.txt', 'r') as archive:
        lines = archive.readlines()
        account_source = input('Enter the account source, so I can search for it.:').strip
        find = False
        line()
        for c in range(3, len(lines)):
            if account_source in lines[c]:
                user_password = line[c].split
                print(f"this is the user {user_password[0]} and that's the password{user_password[2]}")
                find = True
        if find == False:
            print("Sorry but the account which you're seaching don't exists") 
        line()

def generate_password():
        """
        generate a secure password for the user
        """
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
        password = ''.join(random.choice(characters) for i in range(12))
        return password

def security_check(key_access, color):
    """
    Checks if the user which want to see the passwords or write a new one, knows the Key access;
    """
    key = input('Enter you access key: ').strip()
    if key == key_access:
        return True
    else:
        print(f'{color}WRONG KEY!!!, I will stop the program.')
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
        Register a login for the user and create a password for the account
        """
        with open('data_passwords.txt', 'a') as archive:
            archive.write(f'{self.username:<30}{self.login_place:^20}{self.password:>20}\n')