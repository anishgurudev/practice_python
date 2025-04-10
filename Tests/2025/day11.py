
vegetables = {"carrot", "lettuce", "broccoli", "onion"}
vegetables.add("potato")
vegetables.update(["potato", "pumpkin"])
vegetables.remove("lettuce")

print(vegetables)  # {'lettuce', 'broccoli', 'onion', 'potato', 'carrot'}
letters = {"a", "b", "c"}
numbers = {1, 2, 3}
#union is very similar to the update method, but union creates a new set, while update modifies an existing set.
letters_and_numbers = letters.union(numbers)
print(letters_and_numbers)  # {'a', 'c', 1, 2, 3, 'b'}

#1) Create an empty set and assign it to a variable.
seta = set()
print(seta)

# 2) Add three items to your empty set using either several add calls, or a single call to update.
seta.add(1)
seta.add("ram")
seta.update(["2", 3, "rohit","ram"])
print(seta)

# 3) Create a second set which includes at least one common element with the first set.
seta2 = {1,"ajay", "anish", "ankita","2","2"}
print(seta2)
# 4) Find the union, symmetric difference, and intersection of the two sets. Print the results of each operation.
seta1 = seta.union(seta2)
print(seta1)
print(seta.union(seta2))
print(seta.symmetric_difference(seta2))
print(seta2.symmetric_difference(seta))
print(seta.intersection(seta2))
# 5) Create a sequence of numbers using range, then ask the user to enter a number. Inform the user
# whether or not their number was within the range you specified.
user_no = int(input("Enter a no: "))
valid_no = range(1,10,2)
if user_no in valid_no:
    print("your no is in list: ")
else:
    print("your no is not in list: ")
