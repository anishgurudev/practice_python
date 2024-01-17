# Write a program to print all prime no between two numbers

print("Enter two numbers: ")
a = int(input())
b = int(input())
print("prime no between:",a,"and" , b,"is :")
for num in range(a,b):
    i = 2
    while i < num:
        if num % i == 0:
            break
        i = i + 1
    if num == i:
        print(num , end=" ")

