names = ["mary", "Richard", "Noah", "KATE"]
names = [name.title() for name in names]
print(names)

names = {name.title() for name in names}
print(names)
# print(Set_names)
ages = (36, 21, 40, 28)
student_ids = (112343, 134555, 113826, 124888)

people = [
    (name.title(),age)
     for name,age in zip(names,ages)]
print(people)



Student = {student_id: name.title()
           for student_id,name in zip(student_ids,names)}
print(Student)