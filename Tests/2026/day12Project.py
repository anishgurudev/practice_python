from openpyxl.styles.builtins import title

readingList= [] #list
menu_prompt = """ 

Please enter one option

- 'a' for add the book
- 'l' for list the book
- 'q' to quit

what would you like to do ?  """

selected_option= input(menu_prompt).strip().lower()

def add_book():
    print("adding ...")
    title = input("Title: ").strip().capitalize()
    auther = input("Auther: ").strip().capitalize()
    year = input("Year of Publication: ")

    new_book = { "Title": title,
                 "Auther": auther,
                 "year" : year
                 }
    readingList.append(new_book)
    # print(readingList)


def show_book():
    print("displaying ...")
    for book in readingList:
        print(f'{book["Title"]},({book["year"]}) by {book["Auther"]}')


while selected_option!='q':
    if selected_option == "a":
        add_book()
    elif selected_option == "l":
        if readingList :
            show_book()
        else:
            print("you have not read any books!")
    else:
        print(f"Sorry {selected_option}is not the valid options!")
    selected_option = input(menu_prompt).strip().lower()

