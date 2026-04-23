while  True:
    user_number = input("Please enter a whole number: ")
    try:
        number = int(user_number.lstrip("-").isnumeric())
        break
    except ValueError:
        print("You didn't enter a valid integer!")


while True:
    try:
        number = int(input("Please enter a whole number: "))
        break
    except ValueError:
        print("You didn't enter a valid integer!")
