# 1) Define four functions: add, subtract, divide, and multiply. Each function should take two arguments, and they should print the result of the arithmetic operation indicated by the function name.

def add(no1,no2):
    print(no1+no2)


def sub(no1,no2):
    print(no1-no2)


def divide(no1,no2):
    if no2 != 0:
        print(no1/no2)
    else:
        print("enter positive no")


def multiply(no1,no2):
    print(no1*no2)

add(12,5)
sub(12,5)
divide(12,6)
multiply(4,5)
divide(12,0)

#2) Define a function called print_show_info that has a single parameter. The argument passed to it will be a dictionary with some information about a T.V. show. For example:
tv_show = {
    "title": "Breaking Bad",
    "seasons": 5,
    "initial_release": 2008
}
def print_show_info(shows):
    print(f'{shows["title"]} ({shows["initial_release"]}) - {shows["seasons"]} seasons')


print_show_info(tv_show)

#3) Below you’ll find a list containing details about multiple TV series.
series = [
    {"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
    {"title": "Fargo", "seasons": 4, "initial_release": 2014},
    {"title": "Firefly", "seasons": 1, "initial_release": 2002},
    {"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
    {"title": "True Detective", "seasons": 3, "initial_release": 2014},
    {"title": "Westworld", "seasons": 3, "initial_release": 2016},
]
for show in series:
    print_show_info(show)

#4) Create a function to test if a word is a palindrome. A palindrome is a string of characters that are identical whether read forwards or backwards. For example, “was it a car or a cat I saw” is a palindrome.

sentence= "was it a car or a cat I saw"

def palindrome(word):
    reverse = word.lower().replace(" ","")[::-1]
    if reverse == word.lower().replace(" ",""):
        print(f'{word} is a palindrome!')
    else:
        print(f'{word} in not palindrome!')

palindrome(sentence)