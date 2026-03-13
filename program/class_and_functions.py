import random
def line():
    """
    shows a line
    """
    print('—' * 40)



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

def show_logins(self):
    """
    show all accounts created by user
    including the username, password, and account source
    """
    pass

def search_password(self):
    """
    search an especific password and user, with the account source
    """
    pass

def generate_password():
        """
        generate a secure password for the user
        """
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
        password = ''.join(random.choice(characters) for i in range(12))
        return password
    
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
        