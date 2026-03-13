import random
def line():
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


    
class User:
    def __init__(self, name):
        # attributes
        self.name = name
        self.username = ''
        self.login_place = ''
        self.key_access = self.generate_password()
        self.password = self.generate_password()
    
    # methods
    def generate_data(self):
        """
        create a archive where will have data about the user's accounts
        """
        with open('data_passwords.txt', 'w') as archive:
            pass

    def generate_password(self):
        """
        generate a secure password for the user
        """
        characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'
        password = ''.join(random.choice(characters) for i in range(12))
        return password
    
    def menu(self):
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
    def new_login(self):
        """
        Register a login for the user and create a password for the account
        """
        pass
