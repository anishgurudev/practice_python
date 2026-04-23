print(bool(0))              # False
print(bool(6))              # True

print(bool("Caterpillar"))  # True
print(bool(""))             # False

print(bool([]))             # False
print(bool([0, 1, 2, 3]))   # True

print(bool(True))           # True
print(bool(False))          # False
age = int(input("How old are you? "))

if age < 16:
      print("You are eligible for the child rate of 80p.")
elif age >= 60:
      print("You are eligible for the OAP rate of £1.")
else:
      print("You must pay the standard rate of £1.50.")
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print(id(numbers))
print(id(new_numbers))
# numbers = [1, 2, 3, 4]
numbers.append(5)
print(id(numbers))
print(id(new_numbers))

# 3) Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
numbersE =int(input("Enter a no : "))
if numbersE >0 :
    print(f"{numbersE} number is Positive")
elif numbersE < 0:
    print( f"{numbersE} number is negative ")
elif numbersE == 0 :
    print(f"{numbersE} number is Zero! ")
# else: print( " please enter a valid  no!")

# 4) Write a program to determine whether an employee is owed any overtime. You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.

employeeName = input("Enter your name: ")
hourlyRate = float(input("enter your hourly Wage: "))
hourWorked = float(input("How many hours you worked : "))

if hourWorked < 40 :
    print(f'{employeeName} has worked {hourWorked} hours & hourly wage is {hourlyRate}. \n So, earned {hourlyRate * hourWorked}')
elif hourWorked > 40 :
    extraHours = hourWorked- 40
    earning =  (hourlyRate * 40) + (extraHours * hourlyRate * 1.1)
    print(f'{employeeName} has worked for {hourWorked} hours & eligible for overtime : {extraHours} hours and hourly wage is $ {hourlyRate} \n So his total earning is ${earning}')
