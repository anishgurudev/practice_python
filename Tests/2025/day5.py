
# Exercises
# 1) Try to approximate the behaviour of the is operator using ==.
# Remember we have the id function for finding the memory address for a given value,
# and we can compare memory addresses to check for identity.
a = 5
b = 5
print(id(a))
print(id(b))

print(id(a) == id(b))
print(a is b)

c = 89
d = c
print(id(c))
print(id(d))
print(id(c) == id(d))
print(c is d)

list_1 = [1,1,2,2,3]
list_2 = [1,1,2,2,3]
print(id(list_1))
print(id(list_2))
print(id(list_1) == id(list_2))
print(list_1 is list_2)

list_3 = [1,2,3,4,5]
list_4 = list_3
print(id(list_3))
print(id(list_4))
print(id(list_3) == id(list_4))
print(list_3  is list_4)


# 2) Try to use the is operator or the id function to investigate the difference between this:
# numbers = [1, 2, 3, 4]
# new_numbers = numbers + [5]
# And this:
# numbers = [1, 2, 3, 4]
# numbers.append(5)
# Are new_numbers and numbers the same thing? What about numbers before and after we append 5?
# If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay, as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours. In effect, the employees get paid 110% of their hourly wage for any overtime.
numbers = [1, 2, 3, 4]
new_numbers = numbers + [5]
print(id(numbers))
print(id(new_numbers))
# And this: numbers = [1, 2, 3, 4]
print(id(numbers))
numbers.append(5)
print(id(numbers))


# 3) Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
user_number = float(input("Please enter a number: "))
if user_number > 0:
    print(f' {user_number} no is positive')
elif user_number < 0:
    print(f' {user_number} no is negative')
elif user_number == 0:
    print("no is zero")
else:print("dont enter alphabet")






# 4) Write a program to determine whether an employee is owed any overtime.
# You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.
name = input("Please enter your name as employee :  ").strip().title()
hourly_wage = float(input("please let us know your hourly wage: "))
hour_worked = float(input("how many hour you worked in a week: "))
if hour_worked > 40:
    overtime = hour_worked - 40
    print(f"you are eligible for overtime for {overtime} hour")
else:
    print(f"you are not eligible for overtime")

# If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay,
# as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours.
# In effect, the employees get paid 110% of their hourly wage for any overtime.

name = input("Please enter your name as employee :  ").strip().title()
hourly_wage = float(input("please let us know your hourly wage: "))
hour_worked = float(input("how many hour you worked in a week: "))
if hour_worked > 40:
    overtime = hour_worked - 40
    print(f"you are eligible for overtime for {overtime} hour")
    weekly_earning = int((hourly_wage * 40) + (overtime*hourly_wage * 1.1))
    print(f'{name} hourly wage is ${hourly_wage} worked for {hour_worked} hour in a week. So you earned ${weekly_earning} including overtime ${int(overtime*hourly_wage * 1.1)}')

else:
# Regina George earned $800 this week.
    weekly_earning =int(hourly_wage * hour_worked)
    print(f'{name} hourly wage is ${hourly_wage} worked for {hour_worked} hour in a week. So you earned ${weekly_earning}')