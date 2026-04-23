print(1, 2, 3, 4, 5)  # 1 2 3 4 5
print(1, 2, 3, 4, 5, sep= "-" , end="\n\n")
print(1, 2, 3, 4, 5, sep= "|" )  # 1 2 3 4 5


#    *args
# def mul(x, y):
#     print(x * y)
# mul(5, 10)

def mul(*args):
    print(args[0]*args[1])
mul(5, 10) # not right choice

# def multigreet(*args): # we can write like this
def multigreet(*names):
    for name in names:
        print(f"Hello, {name}!")

multigreet("Rolf", "Bob", "Anne", "puchu")

def preety_print(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
preety_print(Title= "the matrix",Director= "wachowski", Year =1990)

def print_movie(*args):
    for value in args:
        print(value)

movie = {
    "title": "The Matrix",
    "director": "Wachowski",
    "year": 1999
}

print_movie(*movie.values())

book_template = "{title}, by {author} ({year})"

def show_books(books):
    # Adds an empty line before the output
    print()

    for book in books:
        print(book_template.format(**book))

    print()
