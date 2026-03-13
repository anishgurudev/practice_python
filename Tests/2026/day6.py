from itertools import count

from numpy.lib.function_base import average
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
  # Check the title of the current movie is Memento
      if movie[0] == "Memento":
            # If the title is Memento, inform the user that the movie exists and break the loop
            print("Memento is in the movie library!")
            break


print(range(0, 10))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers = list(range(10))
print(numbers)
print(list(range(11)))
immutable_numbers = tuple(range(10))
print(immutable_numbers)
print(tuple(range(0,13,2)))

for number in numbers:
    print(number)

employees = [
    ("Rolf Smith", 35, 8.75),
    ("Anne Pun", 30, 12.50),
    ("Charlie Lee", 50, 15.50),
    ("Bob Smith", 20, 7.00)
]
count = 0
total = 0
for employee in employees:
    print(f'{employee[0]} is due to be paid: ${employee[1]* employee[2]}')
print(employees.__len__())
print(len(employees))
#2) For the employees above, print out those who are earning an hourly wage above average.
for employee in employees:
    total = total+ employee[2]
    averageWage= total/ employees.__len__()
    print(total/employees.__len__())

for employee in employees:
    if employee[2] > total/employees.__len__():
        print(f'{employee[0]} is earning above average ')

for number in range(1, 30):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("fizz")
    elif number % 5 ==0:
        print("Buzz")
    else:
        print(number)

for number in range(1, 20):
    if number % 3 == 0:
        if number % 5 == 0:
            print("Fizz Buzz")
        else:
            print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
