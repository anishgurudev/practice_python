# Converting tuples and lists to strings
project_authors = ["Mike", "Sofia", "Helen"]
print(f"The people who worked on this project are: {project_authors}.")

project_authors = ", ".join(project_authors)

print(f"The people who worked on this project are: {project_authors}.")

# user_numbers = input("Please enter 5 numbers separated by commas: ") # 1,2,3,4,5
# numbers_list = user_numbers.split(",")
#
# print(numbers_list) # ['1', '2', '3', '4', '5']
# numbers_tuple = tuple(user_numbers.split(","))
#
# print(numbers_tuple) # ('1', '2', '3', '4', '5')
sample_string = "Python"

print(list(sample_string)) # ['P', 'y', 't', 'h', 'o', 'n']
print(tuple(sample_string)) # ('P', 'y', 't', 'h', 'o', 'n')

#1) Ask the user to enter their given name and surname in response to a single prompt. Use split to extract the names,
# and then assign each name to a different variable. For this exercise, you can assume that the user has a single given name and a single surname.
user_name = input("Please enter your full name : ").split(" ")
print(user_name)
first_name = user_name[0]
last_name = user_name[-1]
middle_name = user_name[-2]
print(first_name)
print(middle_name)
print(last_name)

#2) Print the list, [1, 2, 3, 4, 5], in the format 1 | 2 | 3 | 4 | 5 using the join method. Remember that you can only
#   join collections of strings, so you’re going to need to do some initial processing of the list of numbers.
no_list = [1, 2, 3, 4, 5]
numbers_list = str(no_list).split(",")
print(numbers_list)
sample_string = " | ".join(numbers_list) # ['1', '2', '3', '
print(sample_string)

# print("|".join(str(no_list).split(",")))
base_numbers = [1, 2, 3, 4, 5]
processed_numbers = []

for number in base_numbers:
    processed_numbers.append(str(number))
print(processed_numbers)
print(" | ".join(processed_numbers))



#3) Each quote is a string, but each string actually contains quote characters at the start and end. Using slicing,
# extract the text from each string, without these extra quote marks, and print each quote.
quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]

for quote in quotes:
    print(quote.strip("'"))
# You may also want to try a solution using strip.


#4) 4) Ask the user to enter a word, and then print out the length of the word. You should account for any excess whitespace
# in the user’s input, so you’re going to have to process the string before you find its length.

word = input("Please enter a word: ").strip()

character_count = len(word)
word_count = len(word.split())

print(f"Character count: {character_count}")
print(f"Word count: {word_count}")

