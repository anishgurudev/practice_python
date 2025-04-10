#  Write a short guessing game program using a while loop. The user should be prompted to
#  guess a number between 1 and 100, and you should tell them whether their guess was too high
#  or too low after each guess. The loop should keeping running until the user guesses the number correctly.
target = 37
guess = int(input("Guess the target no: "))
while guess!=target:
    if guess >target:
        print("Too high! ")
    else:
        print("Too low! ")
    guess = int(input("Guess the target no: "))
print("You guessed correctly! ")
# 2) Use a loop and the continue keyword to print out every character in the string "Python", except the "o".
text = "python"
for t in text:
    if t == "o":
        continue
    print(t)
# Remember that strings are collections, and they are iterable, so you can iterate over the string, which will yield one character at a time.

# 3) Using one of the examples from earlier—or a solution entirely of your own—create a program that prints out every prime number between 1 and 100.
primes = []
for dividend in range(2,101):
    for divisor in range(2,dividend):
        if dividend % divisor == 0:
            break
    else:
         primes.append(str(dividend))
print(primes)
print(",".join(primes))