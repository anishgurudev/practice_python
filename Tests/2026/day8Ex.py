userInp = int(input("Guess a no : "))

target = 51
while userInp != target:
    if userInp< target:
        print(f'{userInp} is too low')
    else:
        print(f'{userInp} is too high')
    userInp = int(input("Guess a no : "))
else:
    print(f'{userInp} is correct guess')

text = "python"
for t in text:
    if t=="o":
        continue
    print(t)

prime = []
# create a program that prints out every prime number between 1 and 100.
for dividend in range(2,101):
    for divisor in range(2,dividend):
        if dividend % divisor == 0:
            print(f'{dividend} is not prime!')
            break
    else:
        print(f'{dividend} is prime no!')
        prime.append(str(dividend))
print(prime)
prime = ",".join(prime)
print(prime)
