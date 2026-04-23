from sympy.physics.units import angular_mil

main_characters = [
    ("BoJack Horseman", "Will Arnett", "Horse"),
    ("Princess Carolyn", "Amy Sedaris", "Cat"),
    ("Diane Nguyen", "Alison Brie", "Human"),
    ("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
    ("Todd Chavez", "Aaron Paul", "Human")
]

for name, voice, animal in main_characters:
    print(f'{name} is a {animal.lower()} voiced by {voice}.')

#("John Smith", 11743, ("Computer Science", "Mathematics"))
student= ("John Smith", 11743, ("Computer Science", "Mathematics"))
print(student)

st_name,st_id,(major_s,minor_s)= student
print(student)

#nvestigate what happens when you try to zip two iterables of different lengths. For example, try to zip a list containing three items, and a tuples containing four item
vechale= ("car", "bike", 3)
owner = ("ram", 5 , "anil")
vechaleOwner= zip(vechale,owner)
print(list(vechaleOwner))

