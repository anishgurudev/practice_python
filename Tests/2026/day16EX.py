students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

# def get_name(student):
#     return student["name"]
# students.sort(key=get_name)

students.sort(key=lambda student:student['name'])
print(students)

# convert into lambda
# def exponentiate(base, exponent):
#     return base ** exponent

exp= lambda base,exponent: base ** exponent

# 3) Print the function you created using a lambda expression in previous exercise. What is the name of the function that was created?
print(exp(2,3))
print(exp)
print(type(exp(2,3)))
