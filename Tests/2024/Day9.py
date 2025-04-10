#Day 9: Unpacking, Enumeration, and the zip Function
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

for title, director, year in movies:
    print(f"{title} ({year}), by {director}")


for index in range(len(movies)):
    print(f"{index + 1}. {movies[index][0]} ({movies[index][2]}), by {movies[index][1]}")

# counter = 1
# for title, director, year in movies:
#     print(f"{counter}. {title} ({year}), by {director}")
#     counter += 1

# enumerate
for counter,(title,director,year) in enumerate(movies,start=4):
    print(f"{counter}. {title} ({year}), by {director}")

#zip is an extremely powerful and versatile function used to combined two or more iterables into a single iterable.

pet_owners = ["Paul", "Andrea", "Marta"]
pets = ["Fluffy", "Bubbles", "Captain Catsworth"]

pets_and_owners = zip(pet_owners, pets)
print(list(pets_and_owners))

for owner,pet in zip(pet_owners, pets):
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

movies = zip(movie_titles, movie_directors)

for title, director in movies:
    print(f"{title} by {director}.")

movies_list = list(movies)

print(f"There are {len(movies_list)} movies in the collection.")
print(f"These are our movies: {movies_list}.")
