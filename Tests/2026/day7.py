
print("Super Special Mega Awesome Program\n\nBy Phillip Best")
# Slicing
original_string = "Python"
print(len(original_string))
sliced_string = original_string[0:3] # [:3]
print(sliced_string)  # Pyt

original_string = "Python"
sliced_string = original_string[3:0] # [3:]
print(sliced_string)  # hon

print(original_string[3:])  # hon
print(original_string[3:-1])  # ho





#join : List or Tuple , we can use join
project_authors = ("Mike", "Sofia", "Helen")
project_authors = ", ".join(project_authors)

print(f"The people who worked on this project are: {project_authors}.")

#Split :
user_numbers = input("Please enter 5 numbers separated by commas: ") # 1,2,3,4,5
print(user_numbers)
user_numbers  = user_numbers.split(",")
print(user_numbers)

numbers_list = []

for number in user_numbers:
    numbers_list.append(number.strip())
print(numbers_list) # ['1', '2', '3', '4', '5']


sample_string = "Python"

print(list(sample_string)) # ['P', 'y', 't', 'h', 'o', 'n']
print(tuple(sample_string)) # ('P', 'y', 't', 'h', 'o', 'n')
