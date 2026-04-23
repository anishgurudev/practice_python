#1) Create a function that accepts any number of numbers as positional arguments and prints the sum of those numbers. Remember
# that we can use the sum function to add the values in an iterable.
def sums(*num):
    total = 0
    for nu in num:
        total = total+nu
    return total
print(sums(1,2,4,5))

def multi_add(*numbers):
    print(sum(numbers))

multi_add(1,2,4)

#2) Create a function that accepts any number of positional and
# keyword arguments, and that prints them back to the user.
# Your output should indicate which values were provided as positional arguments,
# and which were provided as keyword arguments.

def arg_printer(*args, **kwargs):
    # print(f"Positional arguments are: {args}")
    # print(f"Keyword arguments are: {kwargs}")
    args = [repr(arg) for arg in args]
    print(f"positional argument are: {','.join(args)}")

    kwargs =[f"{key}={repr(value)}"for key,value in kwargs.items()]
    print(f'keyword arguments are: {",".join(kwargs)}')

arg_printer(1,  "blue",  [1,  23,  3], height=184, key=lambda x: x ** 2)




#3) Print the following dictionary using the format method and ** unpacking
country = {
    "name": "Germany",
    "population": "83 million",
    "capital": "Berlin",
    "currency": "Euro"
}
dis_template = "{name} has {population} population and the capital is{capital} ,There currency is {currency}"

country_template = """Name: {name}
Population: {population}
Capital: {capital}
Currency: {currency}"""

def show_country(kwarg):
    print(dis_template.format(**kwarg))
    print(country_template.format(**kwarg))


show_country(country)

#4) Using * unpacking and range, print the numbers 1 to 20,
# separated by commas. You will have to provide
# an argument for print function's sep parameter for this exercise

print(*range(1,21),sep= ",")

#5) Modify your code from exercise 4 so that each number prints
# on a different line.
# You can only use a single print call.
print(*range(1,21),sep= "\n")
