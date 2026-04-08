#text
example_file = open("example.txt", mode="r")
print(example_file.read())
example_file.close()

write_file = open("ex_write.txt","w")
write_file.write("Welcome to the python writing world, write_example.txt")
write_file.close()

write_file = open("ex_write.txt","a")
write_file.write("\nNow you have two lines! you are learning & growing fast!")
write_file.close()

with open("ex_write.txt", "r") as example_file:
    print(example_file.read())

with open("ex_write.txt","a") as write_file:
    write_file.write("\nNow you are writing 3rd line")
    write_file.close()


#CSV data
with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.read().split("\n")
    print(iris_data)

with open("iris.csv", "r") as iris_file:
    iris_data = iris_file.readlines()
    print(iris_data)

irises = []

for row in iris_data[1:]:
    sepal_length,sepal_width,petal_length,petal_width,species= row.strip().split(",")
    iris_dict = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width,
        "species": species
    }

    irises.append(iris_dict)
print(irises)

with open("iris.csv","r") as iris_file:
    iris_data = iris_file.readlines()
header = iris_data[0].strip().split(",")
irise = []
for row in iris_data[1:]:
    iris = row.strip().split(",")
    iris_dicta = dict(zip(header,iris))

    irise.append(iris_dicta)
print(irise)





