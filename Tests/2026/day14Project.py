from openai.types.graders.score_model_grader_param import Input
from openpyxl.chart.title import Title
from openpyxl.styles.builtins import title

menu_prompt = """ 

Please enter one option

- 'a' for add the book
- 'l' for list the book
- 's' for searching the book
- 'd' for deleting the book
- 'r' for marking as completely read book
- 'q' to quit    

what would you like to do ?  """

selected_option= input(menu_prompt).strip().lower()

def add_book():
    print("adding ...")
    title = input("Title: ").strip().capitalize()
    auther = input("Auther: ").strip().capitalize()
    year = input("Year of Publication: ")
    with open("books.csv","a") as readingList:
        # readingList.write(title,auther,year)
        readingList.write(f"{title},{auther},{year}\n")

def get_all_books():
    books = []
    with open("books1.csv", "r") as readingList:
        for book in readingList:
             Title, Auther, Year = book.strip().split(",")

             books.append({
                    "Title": Title,
                    "Auther": Auther,
                    "Year" : Year
                })

    return books




def show_book(books):
    print("displaying ...")
    for book in books:
        Title, Auther, Year = book.values()
        print(f'{Title},({Year}) by {Auther}')


def searchBook():
    readingList = get_all_books()
    matching_Book = []
    search = input("Enter the book name : ").strip().lower()
    for book in readingList:
        if search in book["Title"].lower():
            matching_Book.append(book)

    return matching_Book


    pass


while selected_option!='q':
    if selected_option == "a":
        add_book()
    elif selected_option == "l":
        readingList = get_all_books()
        if readingList :
            show_book(readingList)
        else:
            print("you have not read any books!")
    elif selected_option == 's':
        matching_Book = searchBook()
        if  matching_Book:
            show_book(matching_Book)
        else:
            print("Sorry no matching book found!")
    elif selected_option == 'd':
        print("selected D")
    elif selected_option == 'r':
        print("selected read")

    else:
        print(f"Sorry {selected_option}is not the valid options!")
    selected_option = input(menu_prompt).strip().lower()

