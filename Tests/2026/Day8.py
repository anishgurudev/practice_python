# prime no: a no is divisible only by itself & 1. for ex 2,3,5,7,11,13,....
from sympy import divisors

#get the num from user
dividend = int(input("please enter a no :" ))
#grab the no one at a time from range sequence
for divisor in range(2,dividend):
    #if no is divisible by divisor , break the loop & print it is not prime no
    if dividend %  divisor == 0:
        print(f'{dividend} is not prime!')
        break
else:
    print(f'{dividend} is prime no!')

#get the num from user
dividend = int(input("please enter a no :" ))
divisor = 2

# Keep looping until the divisor is equal to the user number
while divisor < dividend:
    # if the dividend is divisible but the current divisor , break the loop
    if dividend % divisor == 0:
        print(f'{dividend} is not prime!')
        break
    # increment the divisor for the next irritation
    divisor = divisor +  1
else:
        print(f'{dividend} is prime no!')


































userNumber = int(input("Please Enter a number: "))
while userNumber < 10:
    print("your no is less than 10")
    userNumber = int(input("Enter another no: "))

print("your no was at least be 10 ")

while True :
    option = input("Please enter 'a', 'b' , 'c', or 'q' to quit: ")
    if option== 'a':
        print("you have selected option a!")
    elif option== 'b':
        print("you have selected option b!")
    elif option == 'c':
        print("you have selected option c!")
    elif option == 'q':
        print("you have selected option q for quiting! ")
        break
    else:
        print("You have selected invalid option. ")

# print Even no:
for number in range(10):
    if number % 2 != 0:
        continue
    print(number)

UserInp = int(input("Enter a no : "))
for number in range(UserInp):
    if number % 2 != 0:
        continue
    print(f' no is even:  {number}')

for number in range(UserInp):
    if number % 2 == 0:
        print(f' no {number} is even ')

