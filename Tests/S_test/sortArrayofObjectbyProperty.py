employees = [
    {"name": "Rahul",   "age": 28, "salary": 60000},
    {"name": "Anjali",  "age": 24, "salary": 80000},
    {"name": "Suresh",  "age": 32, "salary": 50000},
    {"name": "Priya",   "age": 22, "salary": 70000},
]
key = lambda x: x["age"]
# For each dict x, return x["age"] as the sort value
#sort by age(ascending)
sort_by_age = sorted(employees,key= lambda x: x['age'])
#sort by sal(ascending)
sort_by_sal = sorted(employees,key=lambda x:x['salary'],reverse=True)
#sort by name(ascending)
sort_by_name = sorted(employees, key= lambda x: x['name'],reverse=False)
for emp in sort_by_name:
    print(emp)
for emp in sort_by_age:
    print(emp)
for emp in sort_by_sal:
    print(emp)