def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid Input"
    return a + b

def subtract(a, b):
    if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
        return "Invalid Input"
    return a - b

def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        return "Invalid Input"
    return a * b

def divide(a, b):
    if a != 0 and b !=0 and isinstance(a,(int,float)) and isinstance(b,(int,float)):
        return a/b
    return "Invalid Input "

print(add(10, "5"))
print(subtract(10, 5))
print(multiply(10, 5))
print(divide(1,0))
print(divide(0,"1"))
print(divide(1.0,0))
print(divide(4,2))


