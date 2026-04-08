def greet(name):
    print(locals())
    greeting = f"Hello, {name}!"
    print(locals())
    print(greeting)

# print(greet("Arpita"))
# print(globals())
print(f"The value of greet('Phil') is {greet('Phil')}.")




names = ["anish", "puchu", "arpita"]
x: 90363
def add(a,b):
    print(locals())
    print(a,b)

add(7, 25)


print(globals())


def add(a, b):
    return a + b

print(add(5,12))
# result = add(5, 12)
# print(result)  # 17

