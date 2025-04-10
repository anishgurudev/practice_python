student = {
    "name": "John Smith",
    "grades": [88, 76, 92, 85, 69]
}

print(student["grades"])  # KeyError

print(student.get("grades", []))  # []
student["age"] = 17
student["age"] = 18

print(student)  # KeyError

movie = {
    "title": "Avengers: Endgame",
    "directors": ["Anthony Russo", "Joe Russo"],
    "year": 2019
}

meta_info = {
    "runtime": 181,
    "budget": "$356 million",
    "earnings": "$2.798 billion",
    "producer": "Kevin Feige"
}

movie.update(meta_info)
print(movie)  # KeyError
movie = {
    "title": "Avengers: Endgame",
    "directors": ["Anthony Russo", "Joe Russo"],
    "year": 2019
}

movie.update({
    "runtime": 181,
    "budget": "$356 million",
    "earnings": "$2.798 billion",
    "producer": "Kevin Feige"
})
print(movie)  # KeyError
