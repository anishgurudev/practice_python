# Write a program to print first n even natural number.
# print 1st 10 even natural no in reverse order - 20 18 16 14 12 10 8 6 4 2

i=2
n = int(input("Enter a number: "))
while n>=i:
    print(n,end=" ")
    n = n - 2


