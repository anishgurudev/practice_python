movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
# extra ) allow users to add more movies to the data set before running the calculations.
new_movie_count = int(input("Enter the no of movie you want to enter:  "))
for _ in range(new_movie_count):
    name =input("Enter movie name : ")
    budget= int(input("Enter the budget of movie : "))
    new_movie = (name,budget)
    movies.append(new_movie)

# 1) Calculate the average budget of all movies in the data set.
total_budget = 0
costly_movies = 0

for movie in movies:
    total_budget = total_budget + movie[1]
print(total_budget)
average_budget = int(total_budget/len(movies))
print(average_budget)

# 2) Print out every movie that has a budget higher than the average you calculated.
# You should also print out how much higher than the average the movie's budget was.
for movie in movies:
    if movie[1] > average_budget :
        print(f'{movie[0]} is higher than average budget by {(movie[1]-average_budget)}')
        costly_movies = costly_movies + 1

# 3) Print out how many movies spent more than the average you calculated.
print(f'{costly_movies:,} movies spent more than the average {average_budget:,}')
