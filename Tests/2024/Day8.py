
# while True:
#     selected_option = input("Please enter 'a', 'b', or 'c', or enter 'q' to quit: ")
#
#     if selected_option == "a":
#         print("You selected option 'a'!")
#     elif selected_option == "b":
#         print("You selected option 'b'!")
#     elif selected_option == "c":
#         print("You selected option 'c'!")
#     elif selected_option == "q":
#         print("You selected option 'q'! Quitting the menu!")
#         break
#     else:
#         print("You selected an invalid option.")

#1) Write a short guessing game program using a while loop. The user should be prompted to guess a number between 1 and 100, and you should tell
# them whether their guess was too high or too low after each guess. The loop should keeping running until the user guesses the number correctly.

# target_number = 47
# guess = int(input("Enter a number: "))
# while guess != target_number:
#     if guess > target_number:
#         print("Too high!")
#     else:
#         print("Too low!")
#     guess = int(input("Enter a number: "))
# print("You guessed correctly!")


#2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
#)Remember that strings are collections, and they are iterable, so you can iterate over the string, which will yield one character at a time.
sample_string = "Python"
exclude = "o"
for character in sample_string:
    if character != exclude:
        print(character)

# for character in sample_string:
#     if character == "o":
#         continue
#     print(character)

#3) Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out every prime number between 1 and 100.
#
# # Get a number to test from the user
# dividend = int(input("Please enter a number: "))
#
# # Grab numbers one at a time from the range sequence
# for divisor in range(2, dividend):
#     # If user's number is divisible by the current divisor, break the loop
#     if dividend % divisor == 0:
#         print(f"{dividend} is not prime!")
#         break
# else:
#     # This line only runs if no divisors produced integer results
#     print(f"{dividend} is prime!")



# for dividend in range(2,101):
#     for divisor in range(2, dividend):
#         # If user's number is divisible by the current divisor, break the loop
#         if dividend % divisor == 0:
#             print(f"{dividend} is not prime!")
#             break
#     else:
#         # This line only runs if no divisors produced integer results
#         print(f"{dividend} is prime!")


primes = []
for dividend in range(2, 101):
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            break
    else:
        # print(dividend)
        primes.append(dividend)
print(primes)

primes = []
for dividend in range(2, 101):
    for divisor in range(2, dividend):
        if dividend % divisor == 0:
            break
    else:
        primes.append(str(dividend))
print(primes)
print(", ".join(primes))
