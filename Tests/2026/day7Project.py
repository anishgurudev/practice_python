from itertools import count

movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

# Calculate the average budget of all movies in the data set.
totalBudget = 0

for movie in movies:
    totalBudget= totalBudget+ movie[1]
print(f'Total Movie Budget is {totalBudget}')

averageBudget = totalBudget/len(movies)
print(f'Average budget is : ${averageBudget}')

count= 0
# Print out every movie that has a budget higher than the average you calculated. You should also print out how much higher than the average the movie's budget was.
for movie in movies:
    if movie[1] > averageBudget:
        print(f'The {movie[0]} is above average budget: ${movie[1]-averageBudget} ')
        count = count+1
# Print out how many movies spent more than the average you calculated.
print(f'There are {count} movies above average budget')

# For the extra part of this assignment, we're going to:
#
# Ask the user how many movies they want to add to the list.
# Use range and a for loop to perform some option the specified number of times.
# Ask the user for a movie name and budget during each iteration of the loop, and append a tuple to the movies list containing this information.
# We'll add this code directly below the definition of our movies variable.

newMovieCount= int(input("Enter how many movie you want "))
for add in range(newMovieCount):
    name= input("Enter new movie name: ")
    budget= int(input("Enter new movie budget: "))
    newMovie = (name, budget)
    movies.append(newMovie)

    
for movie in movies:
    totalBudget = totalBudget + movie[1]
print(f'Total Movie Budget is {totalBudget}')

averageBudget = totalBudget/len(movies)
print(f'Average budget is : ${averageBudget}')

count= 0
# Print out every movie that has a budget higher than the average you calculated. You should also print out how much higher than the average the movie's budget was.
for movie in movies:
    if movie[1] > averageBudget:
        print(f'The {movie[0]} is above average budget: ${movie[1]-averageBudget} ')
        count = count+1
# Print out how many movies spent more than the average you calculated.
print(f'There are {count} movies above average budget')
