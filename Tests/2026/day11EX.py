fruit = set()
# 1) Create an empty set and assign it to a variable.
fruit.add("Mango")
print(fruit)
# 2) Add three items to your empty set using either several add calls, or a single call to update.
fruit.update(["banana","grapes","apple"])
print(fruit)
# 3) Create a second set which includes at least one common element with the first set.
summer_fruit = {"pineApple","Mango","watermelon"}
print(summer_fruit)
# 4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.
# union
print(fruit.union(summer_fruit))
#symmetric difference
print(fruit.symmetric_difference(summer_fruit))
#Intersection
print(fruit.intersection(summer_fruit))
# 5) Create a sequence of numbers using range, then ask the user to enter a number. Inform the user whether or not their number was within the range you specified.
numbers = range(27, 54)
print(5 in numbers)
no =  int(input("Enter a no:  "))
print(no in numbers)
print(13 in numbers)

numbers = range(27, 54)
us_no =  int(input("Enter a no:  "))
if us_no in numbers:
    print(f'{us_no} is in the number')
else:
    if us_no< numbers[0]:
        print("your no is too low")
    else:
        print("your no is too high")
