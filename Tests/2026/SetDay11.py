#Sets are a little different to the collection

vegetables = {"carrot", "lettuce", "broccoli", "onion", "carrot"}

fruit = set()
print(vegetables)
print(fruit)

# nested_sets= {{1,2,3,4},{"a","b","c"}} # illegal in Python
vegetables.add("potato")
print(vegetables)
print(vegetables.pop())
print(vegetables)


vegetables.update(["potato", "pumpkin"])

print(vegetables)  # {'broccoli', 'lettuce', 'carrot', 'potato', 'pumpkin', 'onion'}
vegetables.remove("lettuce")

print(vegetables)  # {'broccoli', 'carrot', 'onion'}

letters = {"a", "b", "c"}
numbers = {1, 2, 3}

letters_and_numbers = letters.union(numbers)

print(letters_and_numbers)  # {'a', 'c', 1, 2, 3, 'b'}
bundle_1 = {"Resident Evil 3", "Final Fantasy VII", "Cyberpunk 2077"}
bundle_2 = {"Doom Eternal", "Halo Infinite", "Resident Evil 3"}
print(bundle_1.difference(bundle_2))  # {'Final Fantasy VII', 'Cyberpunk 2077'}
print(bundle_2.difference(bundle_1))  # {'Halo Infinite', 'Doom Eternal'}
print(bundle_1.symmetric_difference(bundle_2))