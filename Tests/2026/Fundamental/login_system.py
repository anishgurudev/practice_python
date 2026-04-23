'''
🧪 MINI PROJECT: LOGIN SYSTEM (INTERVIEW LEVEL)
🎯 Requirements
User has 3 attempts
Correct password → success
Wrong → retry
After 3 → lock account
'''


def login_system():
    correct_pwd = "test123"
    attempt = 0
    max_attempt = 3
    failed_attempt = []

    while attempt < max_attempt:
        pwd_ip = input("Enter the PWD: ")
        if pwd_ip == correct_pwd:
            print("Welcome Onboard !")
            break
        else:
            failed_attempt.append(pwd_ip)
            print("Wrong Pwd , try agian!")
            attempt = attempt + 1
    else:
        print("Your account is locked! ")
        print(f'Failed attempts: {failed_attempt}')


# login_system()

'''
👉 “User Login Validator”
Features:
Multiple users (list of dict)
Loop through users
Validate password
Print:
success users
failed users
'''
users = [
    {"name": "Anish", "pwd": "test"},
    {"name": "Puchu", "pwd": "test123"}
]
def validate_UN(act_UN,UN):
    return act_UN==UN

def validate_PWD(act_pwd,PWD):
    return act_pwd==PWD

def login_system_D():
    attempt = 0
    failed_attempt = []
    passed_attempt = []
    max_attempts = 3

    while attempt < max_attempts:
        users_name_ip = input("Enter Username:  ").strip()
        for user in users:
            if users_name_ip == user["name"]:
                users_Pwd_ip = input("Enter Password:  ").strip()
                if users_Pwd_ip == user["pwd"]:
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
    else:
        print("🔒 Account Locked!")
    print("Failed Attempts:", failed_attempt)


def login_system_GPT():
    attempt = 0
    failed_attempt = []
    passed_attempt = []
    max_attempts = 3

    while attempt < max_attempts:
        users_name_ip = input("Enter Username: ").strip()
        user_found = False

        for user in users:
            if users_name_ip == user["name"]:
                user_found = True
                users_pwd_ip = input("Enter Password: ").strip()

                if users_pwd_ip == user["pwd"]:
                    passed_attempt.append({
                        "name": users_name_ip,
                        "pwd": users_pwd_ip
                    })
                    print("✅ Welcome Onboard!")
                    print("Failed Attempts:", failed_attempt)
                    print("Passed Attempts:", passed_attempt)
                    return  # don't return → allow tracking
                else:
                    failed_attempt.append({
                        "name": users_name_ip,
                        "pwd": users_pwd_ip
                    })
                    print("❌ Wrong Password, try Again")
                    attempt += 1
                break

        if not user_found:
            failed_attempt.append({
                "name": users_name_ip,
                "pwd": None
            })
            print("❌ Incorrect Username, try again")
            attempt += 1

    if attempt >= max_attempts:
        print("🔒 Account Locked!")

    print("\nFailed Attempts:", failed_attempt)

# login_system_D()

# login_system_GPT()

def login_system_():
    attempt = 0
    failed_attempt = []
    passed_attempt = []
    max_attempts = 3

    while attempt < max_attempts:
        users_name_ip = input("Enter Username:  ").strip()
        for user in users:
            if validate_UN(users_name_ip,user["name"]):
                users_Pwd_ip = input("Enter Password:  ").strip()
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
    else:
        print("🔒 Account Locked!")
    print("Failed Attempts:", failed_attempt)

login_system_()

