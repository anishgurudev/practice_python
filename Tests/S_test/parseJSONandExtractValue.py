#JSON (JavaScript Object Notation) is a lightweight text format to store and transfer data. It looks like a Python dictionary — with key-value pairs.
# Approach 1: Parse a JSON String → Extract Values
# Logic: json.loads() converts a JSON-formatted string into a Python dictionary.
# Then use dict["key"] to extract values
import json

json_string = '{"name": "Rahul", "age": 25, "city": "Mysuru"}'

# Step 1: Parse JSON string → Python dict
data = json.loads(json_string)  # Reads and parses in one step
print(type(data))
print(data)
# Step 2: Extract values using keys
print(data['name'])
print(data['age'])

#Logic: json.load() reads directly from a .json file and
# converts it to a Python dict.

with open("data.json","r") as file:
    datas = json.load(file)  # Reads and parses in one step

print(datas)
print(type(datas))

# Extract top-level key
name = datas['employee']['name']
print(datas['employee'])
print(name)
print(type(name))

# Extract from nested object
city = datas['employee']['address']['city']
print(city)
print(type(city))


#Extract all skill
skill = datas['employee']['skills']
print(skill)
print(type(skill))
for s in skill:
    print(s)
