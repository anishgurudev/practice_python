'''
1) Create a short program that prompts the user for a list
of grades separated by commas. Split the string into individual grades
and use a list comprehension to convert each string to an integer.
You should use a try statement to inform the
user when the values they entered cannot be converted.
'''
import csv
import logging

grade= []

user_input= input("Enter a list of grades separated by comma: ").split(",")
try:
    print(user_input)
    # for marks in user_input:
    #     grade.append(int(marks.strip())
    #     print(marks)
    grade = [int(marks.strip()) for marks in user_input]
except ValueError as e:
    print("The grades you entered were in an invalid format, Error: ",e)
else:
    print(grade)



# 2) Investigate what happens when there is a return statement
# in both the try clause and finally clause of a try statement.

def funct():
    try:
        return "try block code"
    finally:
        return "finally block code "

print(funct()) #finally block code

'''
3) Imagine you have a file named data.txt. Open it for reading using Python,
 but make sure to use a try block to catch an exception that arises 
 if the file doesn't exist. Once you've verified your solution works with 
 an actual file, delete the file and see if your try block is able to 
 handle it.
'''
file_name = input("Enter file name: ")
try:
    with open(file_name,"r") as file:
        reader = file.read()
        if not reader.strip():
            print("empty file")
        else:
            print("\n File Content: ")
            print(reader)
except FileNotFoundError:
    print("Error: Couldn't find data.txt")
except Exception as e:
    logging.error(e)



