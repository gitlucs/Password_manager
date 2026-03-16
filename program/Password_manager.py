from class_and_functions import User
from time import sleep
from class_and_functions import line
from class_and_functions import menu
from class_and_functions import generate_password
from class_and_functions import search_password
from class_and_functions import show_logins
from class_and_functions import security_check
from class_and_functions import create_database
from class_and_functions import init_cryptography
from class_and_functions import read_data
from class_and_functions import save_data
from crypto import transform_hash
import sys
import os

color = {'blue':'\033[1;34m',
         'green':'\033[1;32m',
         'red':'\033[1;31m',
         'none':'\033[m'}

data_file = "database.json"

cryptography = init_cryptography()


#search if is a new login or not
try:
    create_database(data_file)
    key_access = generate_password()
    line()
    print('Welcome, new user! Thanks for using my program.')
    while True:
        name = input(f'Please enter ONLY your first name: ').strip()
        if ' ' in name:
            name = input(f'Please enter ONLY your first name: ').strip()
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
    salt = os.urandom(16)
    data = read_data(data_file)
    data["user_data"]["salt"] = salt.hex()
    data["user_data"]["username"] = name
    data["user_data"]["master_key"] = transform_hash(key_access.encode(), data["user_data"]["salt"], hex = True) 
    save_data(data_file, data)
    
except FileExistsError:
    data = read_data(data_file)
    salt = data["user_data"]["salt"]
    key_access = data["user_data"]["master_key"]
    if security_check(key_access, color['red'], salt) == False:
        sys.exit(0)
    data = read_data(data_file)
    line()
    name = data["user_data"]["username"]
    print(f"Helloo {color['blue']}{name.strip()}{color['none']}, Welcome back!")
    pass

# main program

data = read_data(data_file)
name = data["user_data"]["username"]
key_access = bytes.fromhex(data["user_data"]["master_key"])
salt = data["user_data"]["salt"]
cryptography = init_cryptography()
cryptography.define_key(key_access, salt)

while True:
    menu()
    op = str(input('Write your choice: '))
    while True:
        if op not in '123456':
            op = str(input(f'{color['red']}ERROR! THIS IS NOT AN OPTION{color['none']}, please choice a valid option [1,2,3,4,5,6]: ').strip())
        else:
            break        
    op = int(op)

    if op == 1:
        line()
        show_logins(cryptography)
        sleep(3)

    elif op == 2:
        line() 
        username = str(input('Write the account username: ')).strip()
        place = str(input('Which platform is this account from? ').strip())
        lenght = int(input("Which lenght you want to your password? [We recommend 12 or more] ").strip())
        new_user = User(username, place, lenght)
        new_user.new_login(cryptography)
        print(f'{color['green']}Account successfully registered.{color['none']}')
        print(f'Here is the password for this account: {color['blue']}{new_user.password}{color['none']}')
        sleep(2)

    elif op == 3:
        line()
        if security_check(key_access, color['red']) == False:
            break
        search_password(cryptography)
        sleep(2)

    elif op == 4:
        data = read_data(data_file)
        new_data = data
        delets = 0
        account_del = input('Which account do you want to del? [Enter platform] ')
        for c, b in enumerate(data["accounts"]):
            if account_del == b["place"]:
                new_data["accounts"].pop(c)
                delets +=1
        save_data(data_file, new_data)
        if delets == 0:
            print(f"{color['red']}Account not found")
        else:
            print(f"{color['green']}Account succesfully deleted!{color['none']}")
        sleep(2)

    elif op == 5:
        data = read_data(data_file)
        account_renew = str(input("Which account do you want to recreate password? [Enter platform] ").strip())
        find = 0
        for c, b in enumerate(data["accounts"]):
            if account_renew == b["place"]:
                lenght = int(input("Which lenght you want to your password? [We recommend 12 or more] ").strip())
                new_password = generate_password(lenght)
                print(f"{color['green']}{new_password}{color['none']} That will be you new password for the {color['blue']}{b["place"]}{color['none']} account")
                new_password = cryptography.encrypt(new_password)
                data["accounts"].pop(c)
                b["password"] = new_password
                data["accounts"].insert(c, b)
                save_data(data_file, data)
                find += 1
        if find == 0:
            print(f"{color['red']}Account not found")
        sleep(2)
        
    elif op == 6:
        print('Goodbye!!!')
        break