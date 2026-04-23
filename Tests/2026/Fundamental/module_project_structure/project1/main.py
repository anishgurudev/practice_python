import user
import auth
# from  user import User
# from auth import login

if __name__ == "__main__":
    print("Running directly")

user1 = user.User("anis", "1234")

if auth.login(user1, input("Enter the Pwd: ")):
    print("Login Success")
else:
    print("Wrong Password")
