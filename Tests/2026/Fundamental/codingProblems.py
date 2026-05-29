# 1) Reverse A string
from practice_python.Tests.S_test.coding_problems import result

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