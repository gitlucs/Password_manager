from class_and_functions import User
from time import sleep
from class_and_functions import line
from class_and_functions import menu


color = {'blue':'\033[1;34m',
         'green':'\033[1;32m',
         'red':'\033[1;31m',
         'none':'\033[m'}
user1 = ''
op = 0

#search if is a new login or not
try:
    with open('data_passwords.txt', 'r') as archive:
        print(archive.read(1))
    
except:
    user1 = User(str(input('Please, Enter your name: ')))
    line()
    user1.generate_data()
    print('Welcome new user, Thanks for using my program')
    line()
    print(f'{color['blue']}{user1.key_access}{color['none']} THIS is your new key access to register and see your accounts passwords')
    print('Please save this password in a secure local and not forget her because if it happen you will lost the access of all passwords registers')
    line()
    print('i will wait 10 seconds to you do this:')
    for c in range(1, 11):
        print(c, end = ' ', flush = True)
        sleep(1)
    print('')


# main program
while True:
    menu()
    op = str(input('Write your choice: '))
    while True:
        if op not in '1234':
            op = str(input(f'{color['red']}ERROR! THIS IS A NOT OPTION{color['none']}, please choice a valid option [1,2,3,4]: '))
        else:
            break
    op = int(op) 
    if op == 1:
        user1.show_logins()
    elif op == 2:
        user1.new_login()
    elif op == 3:
        user1.search_password()
    elif op == 4:
        break