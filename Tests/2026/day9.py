# enumerate and zip :

# unpacking: Unpacking is generally used to perform several assignments at once, by extracting the individual values from some iterable. This process is also called destructuring

movie = ("12 Angry Men", "Sidney Lumet", 1957 )
# title = movie[0]
# director = movie[1]
# year = movie[2]

title, director, year = movie
print(year)

movies = [
    (
        "Eternal Sunshine of the Spotless Mind",
        "Michel Gondry",
        2004
    ),
    (
        "Memento",
        "Christopher Nolan",
        2000
    ),
    (
        "Requiem for a Dream",
        "Darren Aronofsky",
        2000
    )
]
for movie in movies:
    print(f'{movie[0]}({movie[2]}), by {movie[1]}')
# unpacking
for name, director,year in movies:
    print(f'{name}({year}), by {director}')


#enumerate
# index = 1
# for name,director,year in movies:
#     print(f'{index}. {name}({year}), by {director}')
#     index=index+1
names = ["Harry", "Rachel", "Brian"]

for counter, name in enumerate(names):
    print(f"{counter}. {name}")

for counter,(name, director, year) in enumerate(movies,start=1):
    print(f'{counter}. {name}({year}), by {director}')


#zip
pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]
petsApet_owners=zip(pets,pet_owners)
print(tuple(petsApet_owners))

pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]
petsApet_owners=zip(pet_owners,pets)
print(list(petsApet_owners))


pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]

for owner, pet in zip(pet_owners, pets):
    print(f"{owner} owns {pet}.")

movie_titles = [
    "Forrest Gump",
    "Howl's Moving Castle",
    "No Country for Old Men"
]

movie_directors = [
    "Robert Zemeckis",
    "Hayao Miyazaki",
    "Joel and Ethan Coen"
]

movies = list(zip(movie_titles, movie_directors))
print(movies)

movie_titles = [
    "Forrest Gump",
    "Howl's Moving Castle",
    "No Country for Old Men"
]

movie_directors = [
    "Robert Zemeckis",
    "Hayao Miyazaki",
    "Joel and Ethan Coen"
]

movies = zip(movie_titles, movie_directors)

for title, director in movies:
    print(f"{title} by {director}.")

movies_list = list(movies)

print(f"There are {len(movies_list)} movies in the collection.")
print(f"These are our movies: {movies_list}.")
