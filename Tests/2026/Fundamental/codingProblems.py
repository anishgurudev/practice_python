# 1) Reverse A string

text = "Automation"
def reverse_string(string):
    return string[::-1]
print(reverse_string(text))

#2) Reverse words in a string
sentence = "hello how are you!          "
def reverse_sentence(sentence):
    res = ""
    for word in sentence.strip().split(" "): #['hello', 'how', 'are', 'you!']
        res = word + " " + res
    return res

print(reverse_sentence(sentence))

#3)Reverse each word individually but keep the word order same
results = " ".join([word[::-1] for word in sentence.split()])
print(results)

#2nd way
#step1: split into words
words = sentence.split()
print(words)#['hello', 'how', 'are', 'you!']
#step2: reverse the words
reverse_words = [word[::-1] for word in words]
print(reverse_words)#['olleh', 'woh', 'era', '!uoy']
#step3:join Back
result= " ".join(reverse_words)
print(result)#olleh woh era !uoy

#4) Reverse String — Keep Numbers & Special Chars in Place
def reverse_letter_only(s):
    # Step 1: Extract only letters
    letters = [c for c in s if c.isalpha()]
    # Step 2: Reverse the letters
    letters.reverse()
    # Step 3: Put letters back, keep others in place
    results = []
    letter_index= 0

    for char in s:
        if char.isalpha():
            results.append(letters[letter_index])
            letter_index+=1
        else:
            results.append(char)
    return "".join(results)

print(reverse_letter_only("Welcome to Python 3.6"))

#5)Write a programme to count the unique charactor or longest substring
s = "abcabcbdb"
no = ["1","2","3","4","5","2","4","1"]
nos = [1,4,5,5,3,5,2,3]
def longest_substring(s):
    seen = set()
    dup = set()
    for ch in s:
        if ch in seen:
            dup.add(ch)
        else:
            seen.add(ch)
    return seen
print(longest_substring(s))
print(longest_substring(no))
print(longest_substring(nos))

#6)write a program for finding non repeating charactor
from collections import Counter
count = Counter(s)
for ch in s:
    if count[ch]==1:
        print(ch)
        break

#7)count vowel in a string
def count_vowel(s):
    # vowels = {"a","e","i","o","u"}
    vowels = "aeiou"
    count = 0
    for ch in s.lower().strip():
        if ch in vowels:
            count =count+1
    return count
print(count_vowel("Automation"))
print(count_vowel("Hello world"))
#2) way 2
def show_vowel_count(s):
    vowels = {"a","e","i","o","u"}
    freq = Counter(char for char in s.lower() if char in vowels)
    return dict(freq)
print(show_vowel_count("Hello world"))

#8)count charactor occurrence
def char_count(s):
    return dict(Counter(s))
print(char_count("Automation"))
print(Counter("Automation"))
print(dict(Counter("Automation")))

def count_vowel_charactor(s):
    vowel = "aeiou"
    vow=[]
    cons=[]
    for ch in s.lower().strip():
        if ch in vowel:
            vow.append(ch)
        else:
            cons.append(ch)
    return vowel.__len__() ,cons.__len__()
vowel, constant = count_vowel_charactor("automation")
print(vowel,constant)
print(f"vowel : {vowel} & contant: {constant}, in the string")

words = ["Flight", "Flow", "Florida", "Flower", "Floor", "Flour"]


def longest_prefix(words):
    if not words:
        return ""
    result = ""

    for char in zip(*words):
        if len(set(char)) == 1:
            result += char[0]
        else:
            break
    return result


print(longest_prefix(words))