# Write a program to print sum of first n natural number.
i=1
sum = 0
n = int(input("Enter a number: "))
while i<=n:
    sum = sum + i
    print(sum)
    i = i + 1
print("Sum of first ",i-1," is",sum)



