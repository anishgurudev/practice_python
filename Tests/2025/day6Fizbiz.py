# day 6 Project Fizz Buzz

# numbers = list(range(1,101))
# print(numbers)
# for number in numbers:
#     no = int(input("Enter any random no between 0 to 100 for playing FizzBuzz: "))
#     if no % 15 == 0:
#         print(f"{no} is Fizz Buzz")
#     elif no % 5== 0:
#         print(f"{no} is Buzz")
#     elif no % 3 == 0:
#         print(f"{no} is Fizz ")
#     else:
#         print(f"{no} is not valid, you loose.\n Better luck next time! ")
#         break

# another way
# numbers = list(range(1,101))
#
# for number in numbers:
#     if number % 3 == 0:
#         if number % 5 == 0:
#             print(f"{number} is Fizz Buzz")
#         else:
#             print(f"{number} is Fizz ")
#     if number % 5 == 0:
#         print(f"{number} is Buzz ")

#another way

# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("Fizz Buzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# another way

numbers = list(range(1,101))
print(numbers)
for number in numbers:
    if number % 15 == 0:
        print(f"{number} is Fizz Buzz")
    elif number % 5== 0:
        print(f"{number} is Buzz")
    elif number % 3 == 0:
        print(f"{number} is Fizz ")
    else:
        print(f"{number} ")