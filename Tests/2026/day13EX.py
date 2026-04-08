#Define a exponentiate function that takes in two numbers. The first is the base, and the second is the power to raise the base to. The function should return the result of this operation. Remember we can perform exponentiation using the ** operator.

def exponential(base,exponent):
    res = base**exponent
    return print(res)

print(exponential(2,3))

#2) Define a process_string function which takes in a string and returns a new string which has been converted to lowercase, and has had any excess whitespace removed.

def process_string(string):
    return print(string.replace(" ","").lower())

process_string("Cat mouse")

#3 Write a function that takes in a tuple containing information about an actor and returns this data as a dictionary. The data should be in the following format:
#("Tom Hardy", "English", 42)  # name, nationality, age

def dictify(actor):
    name , nationality , age = actor

    return {
        "name" : name,
        "nationality": nationality,
        "age" : age
    }

# ) Write a function that takes in a single number and returns True or False depending on whether or not the number is prime
def is_prime(dividend):
    if dividend<2:
        print(f'{dividend} is not prime no!')
        return False
    for divisor in range(2,dividend):
        if dividend % divisor == 0:
            print(f'{dividend} is not prime no!')
            return False
        else:
            print(f'{dividend} is prime')
            return True

is_prime(1)
