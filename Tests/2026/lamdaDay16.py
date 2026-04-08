numbers = [56, 3, 45, 29, 102, 30, 73]
highest_number = max(numbers)

print(highest_number)  # 102

students = [
    {"name": "Hannah", "grade_average": 83},
    {"name": "Charlie", "grade_average": 91},
    {"name": "Peter", "grade_average": 85},
    {"name": "Rachel", "grade_average": 79},
    {"name": "Lauren", "grade_average": 92}
]

def get_grade_average(student):
    return student["grade_average"]
# lambda student : student["grade_average"

for student in students:
    print(get_grade_average(student))

# winner = max(students,key=get_grade_average)
winner = max(students,key=lambda student: student['grade_average'])
print(winner)

def get_name(student):
    return student['name']




# def add(a, b):
#     print(a + b)
#
# def subtract(a, b):
#     print(a - b)
#
# def multiply(a, b):
#     print(a * b)

def divide(a, b):
    if b == 0:
        print("You can't divide by 0!")
    else:
        print(a / b)

operations = {
    "a": lambda a,b: a+b,
    "s": lambda a,b: a-b,
    "m": lambda a,b: a*b,
    "d": divide
}

selected_option = input("""Please select one of the following options:

a: add
s: subtract
m: multiply
d: divide

What would you like to do? """)

operation = operations.get(selected_option)

if operation:
    a = int(input("Please enter a value for a: "))
    b = int(input("Please enter a value for b: "))

    operation(a, b)
else:
    print("Invalid selection")

#Exersice

