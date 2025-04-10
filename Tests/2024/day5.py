age = int(input("How old are you? "))

if age < 18:
      print("Sorry, we can't serve you.")



a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))  # We can use a function called id to find out where something is being stored
print(id(b))  # This long series of numbers is an address that references a location in memory

print(a == b)  # True
print(a is b)  # False

x = [1, 2, 3]
y = x

print(id(x))  # 139685763327296
print(id(y))  # 139685763327296

print(x == y)  # True
print(x is y)  # True


# Exercises
# 1) Try to approximate the behaviour of the is operator using ==. Remember we have the id function for finding the memory address for a given value, and we can compare memory addresses to check for identity.
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
print(numbers is new_numbers)

numbers = [1, 2, 3, 4]
print(id(numbers))

new_numbers = numbers.append(5)
print(id(numbers))



# 3) Ask the user to enter a number. Tell the user whether the number is positive, negative, or zero.
no = int(input("Enter a number: "))
if no==0:
    print(f"no entered is zero: {no}")
elif no>0:
    print(f"no entered is positive: {no}")
elif no<0:
    print(f"no entered is negative : {no}")
else:
    print(f"dont enter alpha: {no}")



# 4) Write a program to determine whether an employee is owed any overtime.
# You should ask the user how many hours the employee worked this week, as well as the hourly wage for this employee.

emp_name= input("Inter your name: ").title().strip()
hourly_wage = float(input("Enter your hourly wage:  "))
hour_worked = float(input("how many hours the employee in a day: "))*5
# If the employee worked more than 40 hours, you should print a message which says the employee is due some additional pay,
# as well as the amount due. The additional amount owed is 10% of the employees hourly wage for each hour worked over the 40 hours.
# In effect, the employees get paid 110% of their hourly wage for any overtime.
week_earning = int(hourly_wage * hour_worked)
if hour_worked>40:
    extra_hours= hour_worked-40
    extra_pay=extra_hours*(hourly_wage*10/100+hourly_wage)
    print(f"the employee is due some additional pay of ${week_earning} + 10% of extra hour ${extra_pay} ")
else:
    print(week_earning)





#
#
# employee_name = input("Enter the employee's name: ")
# hours_worked = float(input(f"How many hours did {employee_name} work this week? "))
# hourly_wage = float(input(f"What is {employee_name}'s hourly wage? "))
#
# if hours_worked > 40:
#     regular_pay = 40 * hourly_wage
#     overtime_pay = (hours_worked - 40) * hourly_wage * 1.1
#     owed_pay = int(regular_pay + overtime_pay)
# else:
#     owed_pay = int(hours_worked * hourly_wage)
#
# print(f"{employee_name} is owed ${owed_pay}.")




