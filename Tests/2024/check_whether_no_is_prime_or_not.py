# Write a program to check whether no is prime or not
# Prime numbers are natural numbers that are divisible by only 1 and the number itself
# logic:no number should divide X  2 to X-1 inside that we are checking x modulus is equal to 0
# then break else continue the loop till X
# now check whether X is equal to i or not (if loop is run with no match then it is prime,
# if it break in middle then it is not prime

num = int(input("Enter a no to check prime or not : "))
i = 2
while i < num:
    if num % i == 0:
        break
    i = i+1
if num == i:
    print(num, "is prime number")
else:
    print(num, "is not prime number")

# print(num, "is prime number") if (num == i) else print(num, "is not prime number")
