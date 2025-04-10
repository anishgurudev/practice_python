print("Hello, World!".lower() )      # "hello, world!"
"Hello, World!".upper()       # "HELLO, WORLD!"
"Hello, World!".capitalize()  # "Hello, world!"
"hello, world!".title()       # "Hello, World!"
"  Hello, World!  ".strip()  # "Hello, World!"
user_name = " ROLF SMITH  "
print(user_name)
user_name = user_name.strip() # "ROLF SMITH"
print(user_name)
user_name = user_name.title()  # "Rolf Smith"
print(user_name)

#Exercise
title = "Joker"
director = "Todd Phillips"
release_year = 2019
#Joker (2019), directed by Todd Phillips
print(f'{title} ({release_year}), by {director}')


#1)The user should be given three prompts where they'll be asked to provide different information about an employee.
# One prompt should ask for the employee's name, another should ask for their hourly wage, and
# the final one should ask how many hours the employee worked this week.
# The employee name should be processed to ensure that it's in a particular format.
# All employee names should be stripped of any excess white space, and should be in title case.
# This means that each word is capitalised with all other letters being lowercase.
# For example, if the employer accidentally has caps lock on and they
#The employee's total earnings for the week should be calculated by multiplying the hours worked by their hourly wage.
#Remember that any user input we receive is going to be a string. While we can multiply strings,
# it won't quite do what you want in this case. It's also worth keeping in mind that the employee's wage,
# or the numbers of hours they worked, might not be a whole number.
#After processing the employee's name and calculating their earnings for the week,
# the program should output this information as a single string.
# For example, output like this would be appropriate:

emp_name= input("Inter your name: ").title().strip()
hourly_wage = float(input("Enter your hourly wage:  "))
hour_worked = float(input("how many hours the employee in a day: "))*5

print(emp_name)
print(hourly_wage)
print(hour_worked)
week_earning = int(hourly_wage * hour_worked)

print(f"Employee {emp_name} earned {hourly_wage} * {hour_worked}= ${week_earning} this week ")
