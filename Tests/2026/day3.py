title = "Joker"
director = "Todd Phillips"
release_year = 2019

print(f'{title} ({release_year}), directed by {director}')

# project of Day 3

name = input("Please enter the employee's name: ").strip().capitalize()
hourly_wage = float(input("What is their hourly wage? "))
hours_worked = float(input("How many hours have they worked this week? "))

print(f'{name} earned ${hourly_wage*hours_worked} this week')