simpsons = ["Homer", "Marge", "Bart", "Lisa", "Maggie"]
simpsons.sort()

print(simpsons)  # ["Bart", "Homer", "Lisa", "Maggie", "Marge"]

# dictaionary : {}

dick = {"key": "value"}

student = {
    "name": "anish",
    "grade": [1,2,3 ],
    "id": 1,
    3: 2,
    "try": {1,3,4,4},
    "tuple": (1,2,3)

}
print(student)
print(student["id"])
print(student["try"])
print(student.get("tuple"))
print(student.values())
print(student.get("grades","not available"))

student["age"] = 17
student.update({"age": 19})
print(student)

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
print(movie)
movie.update(meta_info)
print(movie)
del movie["producer"]
print(movie)
# for at in movie:
#     print(at)
for key in movie.values():
    print(key)

for vlu in movie.keys():
    print(vlu)

for key,value in movie.items():
    print(f'{key}: {value}')
