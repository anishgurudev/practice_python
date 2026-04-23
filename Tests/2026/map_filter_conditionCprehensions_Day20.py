#A quick recap of comprehensions
names = ["tom", "scooby", "scrapy"]
names = [name.title() for name in names]
names = set(names)
names = {name for name in names}
print(names)


#The map Function

def cube(number):
    return number ** 3


numbers = [1, 2, 3, 4, 5]
cubeed_nu = map(cube, numbers)
print(cubeed_nu)
print(list(cubeed_nu))

# print(*cubeed_nu, sep=",")
for no in cubeed_nu:
    print(no)


# map with multiple iterables
def add(a, b):
    return a + b
lambda a,b : a+b # lambda

odd = [1, 3, 5, 7, 9]
even = [2, 4, 6, 8, 10]
# total = map(add, odd, even)
total = map(lambda a,b:a+b ,odd ,even)
print(total)
print(*total, sep=",")
total = list(map(add, odd, even))
print(total)

#map with lambda expressions
lambda a, b: a + b
numbers = [1, 2, 3, 4, 5]
cubed_nu = map(lambda no: no ** 3, numbers)
print(*cubed_nu)

#The operator module
from operator import methodcaller
names = ["tom", "dick", "harry"]
title_name = map(methodcaller("title"), names)
print(list(title_name))

#Conditional comprehensions
numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_no = [no for no in numbers if no % 2 ==0]
print(even_no)
even_nos= []
for no in numbers:
    if no %2 ==0:
        even_nos.append(no)

print(even_nos)

def is_even(no):
    return no % 2 ==0
numbers = [1, 56, 3, 5, 24, 19, 88, 37]
even_nos1 = filter(is_even,numbers)
print(*even_nos1,sep= ",")

#Using None with filter
values = [0, "Hello", [], {}, 435, -4.2, ""]
truthy_values = filter(None, values)
print(*truthy_values)