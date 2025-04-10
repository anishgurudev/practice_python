from numpy.ma.extras import average
from openpyxl.styles.builtins import total

movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]

for movie in movies:
      print(f"{movie[0]} ({movie[2]}), by {movie[1]}")


#1) Below we've provided a list of tuples, where each tuple contains details about an employee of a shop:
employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
# their name, the number of hours worked last week, and their hourly rate.
for employee in employees:
    total_pay = employee[1]* employee[2]
    print(f"{employee[0]} worked for {employee[1]}hrs and his hourly pay is ${employee[2]},so his total due pay is ${total_pay}")
# Print how much each employee is due to be paid at the end of the week in a nice, readable format

#2) For the employees above, print out those who are earning an hourly wage above average.
total_wages = 0
count = 0
for employee in employees:
    total_wages = total_wages + employee[2]
    count = count +1

average_pay = total_wages/count
for employee in employees:
    if employee[2]> average_pay:
        print(f"{employee[0]} is earning above ${average_pay} as his hourly pay is ${employee[2]}")
# Hint: you can use a for loop and two variables to keep track of the total wage and the number of employees. Then, use the two variables to calculate the average.
# Finally, add another loop that goes through the employees list again and prints out only those who have an hourly wage above the calculated average.

