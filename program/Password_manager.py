from class_and_functions import User
from time import sleep
from class_and_functions import line
from class_and_functions import menu
from class_and_functions import generate_password
from class_and_functions import search_password
from class_and_functions import show_logins
from class_and_functions import security_check


color = {'blue':'\033[1;34m',
         'green':'\033[1;32m',
         'red':'\033[1;31m',
         'none':'\033[m'}

op = 0

#search if is a new login or not
try:
    with open('data_passwords.txt', 'x') as archive:
        key_access = generate_password()
        line()
        print('Welcome new user, Thanks for using my program')
        while True:
            name = input(f'Please, write ONLY your first name: ')
            if ' ' in name:
                name = input(f'Please, write ONLY your first name: ')
            else:
                break
        line()
        print(f'{color['green']}{key_access}{color['none']} THIS is your new key access to register and see your accounts passwords')
        print('Please save this password in a secure local and not forget her because if it happen you will lost the access of all passwords registers')
        line()
        print('i will wait 10 seconds to you do this:')
        for c in range(1, 11):
            print(c, end = ' ', flush = True)
            sleep(1)
        print('')
        archive.write(f' {name:<15}{key_access}\n')
        archive.write(f'{'-' * 70}\n')
        archive.write(f'{'Username':<30}{'Account source':^20}{'password':>20}\n')
        
    
except FileExistsError:
    with open('data_passwords.txt', 'r') as archive:
        line()
        print(f'Helloo {color['blue']}{archive.readline().split()[0]}{color['none']}, Welcome back!')
        pass

# main program

with open('data_passwords.txt', 'r') as archive:
    list = archive.readline().split()
    name = list[0]
    key_access = list[1]

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
        print(f'{color['green']}You have successfully registered{color['none']}')
        print(f'And thats is your password for this account: {color['blue']}{new_user.password}{color['none']}')
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