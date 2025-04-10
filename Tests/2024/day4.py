# Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name, the release year of the movie, and the movie’s budget.

#movie= "movie_title", "director_name", "release_year", "movie_budget"
movie = ("stree2" , "pankaj tripathi ", "2024 ", " $ 120000000 ")
movies = [movie]

print(movies)

# Use the input function to gather information about another movie. You need a title, director’s name, release year, and budget.
movie_title = input("Enter movie name :  ")
movie_director_name = input("Enter movie director  name :  ")
movie_release_year = input("Enter movie release year :  ")
movie_budget = input("Enter movie budget :  ")

# Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.
movie1 = (movie_title, movie_director_name, movie_release_year, movie_budget)

# Use an f-string to print the movie name and release year by accessing your new movie tuple.
print(f"{movie1[0]} and ({movie1[2]})")

# Add the new movie tuple to the movies collection using append.
movies.append(movie1)
# Print both movies in the movies collection.
print(movies)
# Remove the first movie from movies. Use any method you like.
del movies[0]
# You can find solutions for these exercises here.
print(movies)
names = "John", "Sarah", "Alice"
print(names[2])

movie= "movie_title", "director_name", "release_year", "movie_budget"
movies =[movie]
movie_title = input("Enter movie title: ")
director_name = input("Enter director_name: ")
release_year = input("Enter release_year: ")
movie_budget = input("Enter movie_budget: ")
new_movie= (movie_title,director_name,release_year,movie_budget)
print(f"{new_movie[0]} and {new_movie[2]}")
movies.append(new_movie)
print(movies)
print(movies[0])
print(movies[1])

del movies[0]
print(movies)