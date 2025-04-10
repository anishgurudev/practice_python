


numbers = list(range(1, 101))
for number in range(1, 101):
    if number % 3 == 0:
        if number % 5 == 0:
            print("fizz-Buzz")
        else:
            print("fizz")
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)
print("00000000000000000000o")

for number in range(1, 101):
    if number % 15 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
print("00000000000000000000o00000000000000000000o00000000000000000000o00000000000000000000o00000000000000000000o00000000000000000000o00000000000000000000o00000000000000000000o")

numbers = list(range(1, 101))
for number in range(1, 101):
    if  number % 3 == 0 and number % 5 == 0:
        print("fizz-Buzz")
    elif number % 5 == 0:
        print("buzz")
    elif number % 3 == 0:
        print("fizz")
    else:
        print(number)