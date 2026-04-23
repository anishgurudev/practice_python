'''
1. CORE IDEA: “Errors Are Inevitable”
In real-world automation, things WILL fail:
Element not found
File missing
Wrong input
API timeout
👉 Your job is NOT to avoid errors
👉 Your job is to handle them smartly

👉 An exception is a runtime error
👉 “Try this… if it fails, do this instead”
'''
import csv
import logging
from logging import error

try:
    print(10 / 0)
# except ValueError:
#     print("Value error")
# except ZeroDivisionError:
#     print("no should not be divisible by zero!")
except Exception as e:
    # print("Error: ",e)
    logging.error(e)

class InvalidAgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
except ValueError:
    print("Invalid input: Enter in digits!")
else:
    print(age)

def check_age(age):
    if age < 18:
        raise InvalidAgeError("Age must be above 18+ ")
try:
    check_age(15)
except InvalidAgeError as e:
    print("Error: ", e)


try:
    with open("login_system.py","r") as file:
        data= csv.reader(file)
        print(data)
        for x in data:
            print(x)
except FileNotFoundError:
    print("File missing")
except UnicodeDecodeError:
    print("Enter a valid file !")


'''
👉 Build: Safe Login System
🎯 Requirements
User has 3 attempts
Correct password → success
Wrong → retry
After 3 → lock account

Requirements:
Handle invalid input
Retry login
Prevent crash

'''
users = [
    {"name": "Anish", "pwd": "test"},
    {"name": "Puchu", "pwd": "test123"}
]
def validate_UN(users_name_ip, param):
    return users_name_ip== param
def validate_PWD(users_Pwd_ip, param):
    return users_Pwd_ip== param
def login_system_():
    attempt = 0
    failed_attempt = []
    passed_attempt = []
    max_attempts = 3

    while attempt < max_attempts:
        try:
            users_name_ip = input("Enter Username:  ").strip()
            for user in users:
                if users_name_ip =="":
                    attempt += 1
                    raise ValueError("Empty Username is not allowed!")


                if validate_UN(users_name_ip,user["name"]):
                    users_Pwd_ip = input("Enter Password:  ").strip()
                    if users_Pwd_ip =="":
                        attempt += 1
                        raise ValueError("Empty Password is not allowed!")

                    if validate_PWD(users_Pwd_ip,user["pwd"]):
                        passed_attempt.append({
                            "name": users_name_ip,
                            "pwd": users_Pwd_ip}
                        )
                        print("\n\nWelcome Onboard!")
                        print("\nFailed Attempts:", failed_attempt)
                        print("Passed Attempts:", passed_attempt)
                        return
                    else:
                        failed_attempt.append({
                            "name": users_name_ip,
                            "pwd": users_Pwd_ip}
                        )
                        print("Wrong Password, try Again")
                        attempt += 1
                    break
            else:
                failed_attempt.append({
                    "name": users_name_ip,
                    "pwd": None}
                )
                print("Incorrect Username, try again")
                attempt += 1
        except ValueError as e:
            print("Error: ",e)
    else:
        print("🔒 Account Locked!")
    print("Failed Attempts:", failed_attempt)
# login_system_()
def login_system_e():
    attempt = 0
    max_attempt = 5
    while attempt<max_attempt:
        try:
            user_input_un = input("Enter user name: ")
            if user_input_un== "":
                raise ValueError("Empty UN is not allowed")
            for user in users:
                if user_input_un == user["name"]:
                    user_input_pwd = input("Enter Password: ")

                    if user_input_pwd =="":
                        attempt+=1
                        raise ValueError("Empty Password is not allowed: ")

                    if user_input_pwd == user["pwd"]:
                        print("Login Successful!")
                        return
                    else:
                        print("Wrong Password, Try Again!")
                        attempt+=1
                    break
            else:
                attempt+=1
                print("Wrong user name, try again!")
        except ValueError as e:
            attempt += 1
            print("Error: ", e)
    if attempt==max_attempt:
        print("Account locked!")

# def login_system_e():
#     attempt = 0
#     max_attempt = 3
#
#     while attempt < max_attempt:
#         try:
#             user_input_un = input("Enter user name: ").strip()
#
#             if user_input_un == "":
#                 attempt += 1
#                 raise ValueError("Empty username is not allowed")
#
#             user_found = False
#
#             for user in users:
#                 if user_input_un == user["name"]:
#                     user_found = True
#
#                     user_input_pwd = input("Enter Password: ").strip()
#
#                     if user_input_pwd == "":
#                         attempt += 1
#                         raise ValueError("Empty password is not allowed")
#
#                     if user_input_pwd == user["pwd"]:
#                         print("✅ Login Successful!")
#                         return
#                     else:
#                         print("❌ Wrong Password, Try Again!")
#                         attempt += 1
#                     break
#             else:
#                 attempt+=1
#                 print("Wrong user name, try again!")
#
#             # if not user_found:
#             #     print("❌ Wrong username, try again!")
#             #     attempt += 1
#
#         except ValueError as e:
#             print(f"⚠️ Error: {e}")
#
#     print("🔒 Account locked!")
# login_system_e()

def safe_file_reader():
    file_name=input("Enter File name: ")
    try:
        with open(file_name,"r") as file:
            reader= csv.reader(file)
            if not reader.strip():
                print("File is empty")
            else:
                print("\n File Content: ")
                print(file)
    except FileNotFoundError:
        logging.error("File not Found!")
    except Exception as e:
        logging.error(e)

safe_file_reader()
