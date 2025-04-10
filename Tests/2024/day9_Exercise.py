#The data contains the character name, the voice actor or actress who plays them, and the species of the character.

#Write a for loop that uses destructuring so that you can print each tuple in the following format:
#BoJack Horseman is a horse voiced by Will Arnet.


main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]
for character_name,voice,animal in main_characters:
    print(f"{character_name} is a {animal.lower()} voiced by {voice}")


# 2) Unpack the following tuple into 4 variables:
#("John Smith", 11743, ("Computer Science", "Mathematics"))
#The data represents a student's name, their student id number, and their major and minor disciplines in that order.

tup = ("John Smith", 11743, ("Computer Science", "Mathematics"))
# name,id, sub = tup
# major,minor= sub

name, id_number, (major, minor) = tup
print(name,id_number, major,minor)

#3) Investigate what happens when you try to zip two iterables of different lengths. For example, try to zip a list containing three items, and a tuples containing four items.
letters = ["a", "b", "c"]
numbers = [1, 2]

print(list(zip(letters, numbers)))
