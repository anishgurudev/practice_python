#1) Use map to call the strip method on each string
# in the following list:

humpty_dumpty = [
    "  Humpty Dumpty sat on a wall,  ",
    "Humpty Dumpty had a great fall;     ",
    "  All the king's horses and all the king's men ",
    "    Couldn't put Humpty together again."
]
#optin 1
def line_striper(line):
    return line.strip()

print(*map(line_striper,humpty_dumpty), sep="\n")
from operator import methodcaller as ms

#optin 2
striped_rym = map(ms("strip"), humpty_dumpty)
print(*striped_rym, sep="\n")
#optin 3
print(*map(lambda line :line.strip(),humpty_dumpty), sep="\n")


#2) Below you'll find a tuple containing several names:
names = ("bob",
         "Christopher",
         "Rachel",
         "MICHAEL",
         "jessika",
         "francine")
nam8s = []


def small_name(name):
    if name.__len__() < 8:
        return name.title()

sh_name= filter(small_name,names)
print(*sh_name, sep="\n")
#optin 2
names =[name.title() for name in names if name.__len__() <8]
print(names)
#optin 3
nam_title = map(ms("title"),filter(lambda name: len(name)< 8,names))
print(*nam_title)

#3) Use filter to remove all negative numbers from the following
# range: range(-5, 11). Print the remaining numbers to the console.

nos = []
for no in range(-5,11):
    nos.append(no)
    print(no)
print(nos)

def pos_no(no):
    if no > 0:
        return no
posi_no = filter(pos_no,nos)
print(*posi_no, sep=", ")
#optin 1
print(*filter(lambda no :no >0,range(-5,11)))