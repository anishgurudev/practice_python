'''
| Mode | Meaning           |
| ---- | ----------------- |
| r    | read              |
| w    | write (overwrite) |
| a    | append            |
| x    | create            |
open("file.txt", "mode")
👉 “Borrow file → use → auto return”
'''
from os import write

with open("../iris.csv", "r") as file:
    # print(file)
    data = file.read()
    print(data)
    for line in data:
        print(line, end="")

#For creating file
# with open("../report.txt","x") as file:
#     file.write("Test Passed")

with open("../report.txt","a") as file:
    file.write("\nNew line ")

with open("../report.txt","r") as file:
    data = file.read()
    print(data)

# csv

import csv

with open("../iris.csv","r") as file:
    data = csv.reader(file)
    print(data)
    for row in data:
        print(row)

with open("../iris.csv","r") as file:
    data = csv.DictReader(file)
    print(data)
    for row in data:
        print(row)
        print(row["sepal_length"],row["species"])


print("---------------------------------------")
'''
🎯 Task
Read CSV
Count users
Find users > 25
Write report
'''
count = 0
above_25 = []
# read data.csv file
with open("../data.csv", "r") as file:
    data = csv.DictReader(file)
    # find user above 25 and count
    for user in data:
        count+=1
        if int(user["age"])>25:
            above_25.append(user["name"])
    # add to report file
with open("../report.txt","w") as file:
    file.write(f'Total Users: {count}\n')
    file.write(f'User above 25: {above_25}')

#read the report
with open("../report.txt","r") as file:
    print(file.read())
    file.seek(0)
    print("-------")
    print(file.read())
    file.seek(0)
    print(file.read())



