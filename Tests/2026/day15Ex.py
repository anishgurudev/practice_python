# 1) Convert the following for loop into a comprehension:
numbers = [1,2,3,4,5]
# square = []
# for number in numbers:
#     square.append(number**2)
# print(square)

square = [number**2 for number in numbers]
print(square)

# ) Use a dictionary comprehension to create a new dictionary from the dictionary below, where each of the values is title case.
#
movie = {
    "title": "thor: ragnarok",
    "director": "taika waititi",
    "producer": "kevin feige",
    "production_company": "marvel studios"
}

movie = { key.title():value.title()
         for key,value in movie.items()
          }
print(movie)