# Csv

with open("iris.csv", "r") as file:
    iris_data = file.readlines()
    # print(iris_data)

header = iris_data[0].strip().split(",")
# print(header)
irises= []

for row in iris_data[1:]:
    # length,width,p_length,p_width,species = row.strip().split(",")
    # irises.append({
    #     "sepal_length" : length,
    #     "sepal_width":width,
    #     "petal_length":p_length,
    #     "petal_width": p_width,
    #     "species": species
    # })
    iris =row.strip().strip().split(",")
    # print(iris)
    iris_dict = dict(zip(header,iris))
    # print(iris_dict)
    irises.append(iris_dict)
# print(irises)

#Exercise
with open("day14EX.txt","w") as write_file:
    write_file.write("Hello World!")
    write_file.close()
with open("day14EX.txt","a") as update_file:
    update_file.write("\nHow are you doing today?")
    update_file.close()


for irise in irises:

    # print(irise)
    #1 print(f'{irise["sepal_length"]},{irise["sepal_width"]},{irise["petal_length"]},{irise["petal_width"]},{irise["species"]}')

    #2sepal_length,sepal_width,petal_length, petal_width, spieces = irise.values()
    # print(f"{spieces},{sepal_length},{sepal_width},{petal_length},{petal_width}")
    # print(",".join(irise.values()))
    print(",".join(irise.values())+ "\n")
print(",".join(irise.keys()))
