#employee's name, another should ask for their hourly wage, and the final one should ask
# how many hours the employee worked this week
name = input("Please enter your name as employee :  ").strip().title()
hourly_wage = float(input("please let us know your hourly wage: "))
hour_worked = float(input("how many hour you worked in a day: "))
# Regina George earned $800 this week.
weekly_earning = hourly_wage * hour_worked * 5
print(f'{name} hourly wage is ${hourly_wage} worked for {hour_worked} hour in a day. So you earned ${weekly_earning}')


