import json
import os.path

if not os.path.isfile("Data.txt"):
    f = open("Data.txt", 'a')
    f.write('{}')
    f.close()
r = open("Data.txt", 'r')
users_string = r.read()
users_dict = json.loads(users_string)


def login_system():
    condition = int(input("1 For Login 2 For Signup: "))
    if condition == 1:
        old_user()
    if condition == 2:
        new_user()


def new_user():
    input("Name: ")
    input("Phone Number:")
    new_login = input("Email: ")
    if new_login in users_dict.keys():
        print("Email already exists.")
    else:
        password = input("Password: ")
        try:
            users_dict[new_login] = password
            to_write = json.dumps(users_dict)
            f = open("Data.txt", 'w')
            f.write(to_write)
        except Exception as e:
            print(e)
        print("User Created.")


def old_user():
    email = input("Email: ")
    if email in users_dict.keys():
        print("Email Matches.")
    password = input("Password: ")
    stored_password = users_dict[email]
    if stored_password == password:
        print("Successfully Login")
    else:
        print("Wrong Password")


login_system()



