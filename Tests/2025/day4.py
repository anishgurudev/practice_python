#1Create a movies list containing a single tuple. The tuple should contain a movie title, the director’s name,
# the release year of the movie, and the movie’s budget.
movie = ("ved" , "Anish" , "2022" , "1000000")
movies = [movie]
# movies = [("movie_title" ,"director_name" ,"release_year","movie_budget"),]


#2 Use the input function to gather information about another movie. You need a title, director’s name, release year, and budget.
movie_title = input("Enter movie title: ")
director_name = input("Enter movie's director name: ")
release_year = input("Enter movie release year: ")
movie_budget = input("Enter movie budget: ")


#3 Create a new tuple from the values you gathered using input. Make sure they’re in the same order as the tuple you wrote in the movies list.
movies1 = (movie_title , director_name , release_year ,movie_budget )

#4 Use an f-string to print the movie name and release year by accessing your new movie tuple.
print(f'{movies1[0]} is released on {movies1[2]}')


#5 Add the new movie tuple to the movies collection using append.
movies.append(movies1)
print(movies)

#6 Print both movies in the movies collection.
print(movies[0])
print(movies[1])


#7 Remove the first movie from movies. Use any method you like.
print(movies)
movies.pop(0)
#del movies[0]
print(movies)

