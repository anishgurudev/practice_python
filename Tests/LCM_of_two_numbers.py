# Write a program to print lcm(least common multiple) of two numbers
# logic : max(a,b) <= LCM(ab) <= a*b

print("Enter two numbers : ")
a = int(input())
b = int(input())
Max = a if a > b else b
while Max <= a*b:
    if Max%a ==0 and Max%b == 0:
         print("LCM is :",Max)
         break
    Max= Max+1
