#list
names = ["John", "Alice", "Sarah", "George"]
print(names[0])
names.append("Sali")
names = names + ["jija"]
print(names)
numbers = [1, 2, 4, 5]
print(numbers)
numbers.insert(2,3)
print(numbers)
names.remove("Sali")
print(names)
lastName = names.pop()
print(lastName)
print(names)
names.sort()
print(names)

# Tuples

names = "John", "Sarah", "Alice"
print(names)
movies = [
    ("Eternal Sunshine of the Spotless Mind", 2004),
    ("Memento", 2000),
    ("Requiem for a Dream", 2000)
]
print(movies)
print(movies[1][0] ) # "Eternal Sunshine of the Spotless Mind"
print(movies[0])

#exercises

# Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.
movie =("Journey Of Anish","Anish",1990, "$1000000000")
print(movie)
movies = [movie]
print(movies)

#Use the input function to gather information about another movie. You need a title, director’s name, release year, and budget.
movieName = input("Enter movie Title: ")
movieDirector = input(" Enter Director's Name: ")
movieReleaseYear = input("Enter release year: ")
movieBudget= input("Enter movie Budget : ")

#3 Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.
movie1 = movieName,movieDirector,movieReleaseYear,movieBudget
print(movie1)

# Use an f-string to print the movie name and release year by accessing your new movie tuple.

print(f'{movie1[0].capitalize()} , released in {movie1[2]}')

movies.append(movie1)
print(movies)
movies.remove(movies[0])
print(movies)
# extend
l_1 = [1, 2, 3, 4]
t_1 = (5, 6, 7, 8)

l_1.extend(t_1)  # [1, 2, 3, 4, 5, 6, 7, 8]
print(l_1)