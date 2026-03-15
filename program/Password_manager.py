from class_and_functions import User
from time import sleep
from class_and_functions import line
from class_and_functions import menu
from class_and_functions import generate_password
from class_and_functions import search_password
from class_and_functions import show_logins
from class_and_functions import security_check
from class_and_functions import init_cryptography
from class_and_functions import Criptography


color = {'blue':'\033[1;34m',
         'green':'\033[1;32m',
         'red':'\033[1;31m',
         'none':'\033[m'}

op = 0

init_cryptography()
cryptography = Criptography()
try:
    with open("secret.key", "x") as key_file:
        cryptography.define_key()
except:
    cryptography.remember_key()

#search if is a new login or not
try:
    with open('data_passwords.txt', 'x') as archive:
        key_access = generate_password()
        line()
        print('Welcome, new user! Thanks for using my program.')
        while True:
            name = input(f'Please enter ONLY your first name: ')
            if ' ' in name:
                name = input(f'Please enter ONLY your first name: ')
            else:
                break
        line()
        print(f'{color['green']}{key_access}{color['none']} This is your new access key to register and see your accounts passwords')
        print("""Please save this key in a secure place and do not forget it,\n
                because if you lose it you will lose access to all stored passwords.""")
        line()
        print('I will wait 10 seconds for you to do this:')
        for c in range(1, 11):
            print(c, end = ' ', flush = True)
            sleep(1)
        print('')
        archive.write(f'{cryptography.encrypt(f'{name:<15}{key_access})')}\n')
        archive.write(f'{cryptography.encrypt(f'{'-' * 70}')}\n')
        archive.write(f'{cryptography.encrypt(f'{'Username':<30}{'Account source':^20}{'password':>20}')}\n')
        
    
except FileExistsError:
    with open('data_passwords.txt', 'r') as archive:
        line()
        print(f'Helloo {color['blue']}{cryptography.decrypt(archive.archive.readlines()[0])}{color['none']}, Welcome back!')
        pass

# main program

with open('data_passwords.txt', 'r') as archive:
    name = cryptography.decrypt(archive.readlines()[0])
    key_access = cryptography.decrypt(archive.readlines()[1])

while True:
    menu()
    op = str(input('Write your choice: '))
    while True:
        if op not in '1234':
            op = str(input(f'{color['red']}ERROR! THIS IS NOT AN OPTION{color['none']}, please choice a valid option [1,2,3,4]: '))
        else:
            break        
    op = int(op)
    if op == 1:
        line()
        if security_check(key_access, color['red']) == False:
            break
        show_logins()
        sleep(3)

    elif op == 2:
        line() 
        if security_check(key_access, color['red']) == False:
            break
        username = str(input('Write the account username: ')).strip()
        place = str(input('Which platform is this account from? '))
        new_user = User(username, place)
        new_user.new_login()
        print(f'{color['green']}Account successfully registered.{color['none']}')
        print(f'Here is the password for this account:: {color['blue']}{new_user.password}{color['none']}')
        sleep(2)
    elif op == 3:
        line()
        if security_check(key_access, color['red']) == False:
            break
        search_password()
        sleep(2)
    elif op == 4:
        print('Goodbye!!!')
        break