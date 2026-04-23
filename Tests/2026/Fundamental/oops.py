class User:
    def __init__(self, name):
        self.name= name

    def greet(self):
        print("hello", self.name)
user1 = User("Anish")
user1.greet()
print(type(user1))
print(type(user1.name))
print(user1.name)

# 👉 Build: User System (OOP)
class User:
    def __init__(self,name,password):
        self.name = name
        self.password=password

    def login(self, input_password):
        if input_password == self.password:
            print(f"{self.name} logged in")
        else:
            print("Invalid Password!")

user1 = User("Anish", "1234")
user1.login("12345")
user1.login("1234")

class User:
    def login(self):
        print("User login")

class Admin(User):
    def create_user(self):
        print("User created!")
    def delete_user(self):
        print("user deleted")

admin = Admin()
admin.create_user()
admin.delete_user()
admin.login()
# user2 = User()
class User:
    def __init__(self):
        self.__password= "1234"

    def get_password(self):
        return self.__password

user1=User()
print(user1.get_password())

class LoginPage:
    def enter_un(self,un):
        print("Entering Username: ",un)
    def enter_pwd(self,pwd):
        print("Entering Password: ", pwd)
    def click_login(self):
        print("clicked login")

login=LoginPage()
login.click_login()
login.enter_un("anish")
login.enter_pwd("abc")

class User:
    def __init__(self,name):
        self.name= name
user1 =User("ani")
# user1.name
print(user1.name)
