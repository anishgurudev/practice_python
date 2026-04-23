name = input("Enter Your name and surname: ")
name = name.split(" ")
print(name)
firstName = name[0]
lastName = name[1]
print(firstName)
print(lastName)

list = [1, 2, 3, 4, 5]
lista =[]
for l in list:
    lista.append(str(l))
print(lista)
lista="|".join(lista)
print(lista)

quotes = [
    "'What a waste my life would be without all the beautiful mistakes I've made.'",
    "'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
    "'The very essence of romance is uncertainty.'",
    "'We are not here to do what has already been done.'"
]
for quote in quotes:
    print(quote.strip("'"))

wordz = input(" Enter a word or Sentence or your full name: ").strip().capitalize()
wordz= wordz.split(" ")
print(f' Input wordz is containing {wordz}')
print(f' It contains {len(wordz)}  words')
for word in wordz:
    print(f'input Text is : {word}')
    print(f'The Alphabet in Word is : {word.strip().__len__()}')
    print(f'The Alphabet in Word is : {len(word.strip())}')





