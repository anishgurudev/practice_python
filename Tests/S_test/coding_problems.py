# 1) Reverse A string
from sympy import series

string = "Automation"


# string = input("Enter a word: ")

def reverse_string(string):
    return string[::-1]


print(reverse_string(string))

# 2) Check for Palindrome
text = "A man , a plan, a canal: Panama"


def is_palindrome(string):
    string = string.lower()
    return string[::-1] == string


def is_sentence_palindrome(string):
    # Keep only letters/digits, ignore spaces & punctuation
    cleaned_string = "".join(char.lower() for char in string if char.isalnum())
    print(cleaned_string)
    return cleaned_string == cleaned_string[::-1]


print(is_sentence_palindrome(text))

# 3) Check for Duplicate no in array
# Given an Array of , integers, return all elements that appear more than once
# example [1,2,3,4,2,4,5] o/p - 2,4
input = [1, 2, 3, 4, 2, 4, 5]


def find_duplicate(nos):
    seen = set()  # track number we have already visited
    duplicate = set()  # Store confirmed duplicate (avoid re adding)
    for no in nos:
        if no in seen:  # Already visited → duplicate!
            duplicate.add(no)
        else:  # First visit → mark as seen
            seen.add(no)

    return list(duplicate)


# 3) remove the Duplicate no in array
def remove_duplicate(nos):
    seen = set()
    # duplicate = set()
    for no in nos:
        if no in seen:
            pass
        else:
            seen.add(no)
    return list(seen)


def remove_duplicates(nos):
    return list(set(nos))


print(find_duplicate(input))
print(remove_duplicate(input))
print(remove_duplicates(input))

# 4) count vowel in a string
text = "Hello world"


def count_vowel(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}  # set → O(1) lookup
    count = 0
    for s in string.lower().strip():
        if s in vowels:
            count = count + 1
    return count


print(count_vowel(text))

from collections import Counter


def show_vowel_count(string):
    vowels = "aeiou"
    freq = Counter(char for char in string.lower() if char in vowels)
    return dict(freq)


print(show_vowel_count(string))  # {'e': 1, 'o': 2}

# 5) find minm & maxim no in array
# Logic: Python has built-in functions that directly return the min and max.
arr = [3, 5, 4, 1, 9]


def find_min_max(arr):
    return min(arr), max(arr)


min, max = find_min_max(arr)
print(f'min is {min} , max is {max}')

# 6) find second largest no in array
arr = [12, 35, 1, 10, 34, 1]  # second largest = 34


def second_largest(arr):
    arr = sorted(set(arr))
    if len(arr) < 2:
        return None
    return arr[-2]


print(f'second largest no is {second_largest(arr)}')


# 7 Create a Fibonacci series
def fabonacci(n):
    a, b = 0, 1
    series = [a, b]
    for no in range(2, n):
        series.append(a + b)
        a, b = b, a + b
    return series


print(fabonacci(10))  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# 8 Find factorial of number
# Ex
# Input: n = 5
# Output: 120
# Explanation: 5! = 5 * 4 * 3 * 2 * 1 = 120
import math


def factorial(n):
    facto = 1
    i = 2
    # n = int(n)
    # Calculating factorial of number
    while (i <= n):
        facto = facto * i
        i = i + 1
    return facto
    # return 1 if n <=1 else n * factorial(n-1)
    # return math.factorial(n)


print(factorial(5))


# 9 Find prime no
# Input: n = 7
# Output: true
# Explanation: 7 is a prime number because it is greater than 1 and has no divisors other than 1 and itself.

def prime_check(n):
    if n <= 1:
        return False
    # Check divisibility from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(prime_check(17))


def prime(n):
    def is_prime(N):
        for i in range(2, N):
            if N % i == 0:
                return False
        return True

    # Variable to store the number of primes printed so far
    cnt = 0
    # Variable to store the number to be checked for prime
    no = 2
    # Iterate until we have printed the first 10 primes
    for no in range(2, n):
        # while cnt < n:
        if is_prime(no):
            print(no, end=" ")
            cnt += 1
        no = no + 1


prime(10)

#10 swap two no
a, b = 10, 20


def swap(a, b):
    return b, a


print(swap(a, b))

#11) count charactor occurrence
from collections import Counter


def count_char(string):
    return dict(Counter(string))


print(count_char("Automation")) #{'A': 1, 'u': 1, 't': 2, 'o': 2, 'm': 1, 'a': 1, 'i': 1, 'n': 1}


def count_vowel_charactor(string):
    vowel = "a,e,i,o,u"
    vow = []
    cons = []
    for char in string.lower().strip():
        if char in vowel:
            vow.append(char)
        else:
            cons.append(char)
    return vow.__len__(), cons.__len__()


print(count_vowel_charactor("Automations"))
vowel, constant = count_vowel_charactor("Automations")
print(f'Vowel: {vowel} , Constant : {constant} in the String')


#12) Check Odd/Even

def check_even_odd(n):
    # if n % 2 == 0:
    #     return "Even"
    # else:
    #     return "Odd"
    return "even" if n % 2 == 0 else "odd"


print(check_even_odd(4))


#13 Remove Duplicates from String
def remove_duplicate(string):
    # return set("".join(string))
    return "".join(dict.fromkeys(string))


print(remove_duplicate("programming")) #progamin

#14 Armstrong Number check
"""
Examples

Input: n = 153
Output: true
Explanation: 153 is an Armstrong number, 1*1*1 + 5*5*5 + 3*3*3 = 153

Input: n = 9474
Output: true
Explanation: 94 + 44 + 74 + 44 = 6561 + 256 + 2401 + 256 = 9474

Input: n = 123
Output: false
Explanation: 1³ + 2³ + 3³ = 1 + 8 + 27 = 36
"""


def is_armstrong(no):
    # print(type(no))
    s = str(no)  # ✅ Safe now
    # print(type(s))
    print(sum(int(d) ** len(s) for d in s))
    return no == sum(int(d) ** len(s) for d in s)
    # return no == sum(int(d) ** len(s) for d in s)


print(is_armstrong(153))

#15 ) Reverse words in a string
sentence = "hello how are you!          "


def reverse_sentence(sentence):
    res = ""
    for word in sentence.strip().split(" "): #['hello', 'how', 'are', 'you!']
        res = word + " " + res
        # print(res)
    return res


print(reverse_sentence(sentence))#you! are how hello


#16) count word in sentence
def count_word(sentence):
    # Split the sentence into a list of words using whitespace
    words = (sentence.strip().split(" "))
    # Use list comprehension to get the length of each word
    char = [len(word) for word in words]
    # char = list(map(len, sentence.split()))

    # print(words, char)   #['Python', 'is', 'fun', 'and', 'versatile'] [6, 2, 3, 3, 9]
    return char


# Example usage
sentence = "Python is fun and versatile"
result = count_word(sentence)

# Displaying each word with its count
words = sentence.split()
for words, char in zip(words, result):
    print(f'{words}:{char} characters')


def count_word_dict(sentence):
    return {word: len(word) for word in sentence.split()}


print(count_word_dict(sentence))


#17 Anagram check
#An anagram means:
# Same characters
# Same frequency
# Order can be different

def is_anagram(str1,str2):
    return sorted(str1.strip().lower()) == sorted(str2.strip().lower())

print(is_anagram("listen","silent"))


#18 Write a programme to count the unique charactor or longest substring
s = "abcabcbdb"
def longest_substring(s):
    seen= set()
    dupli = set()
    for char in s:
        if char in seen:
            dupli.add(char)
        else:
            seen.add(char)
    return dupli

print(longest_substring(s)) #{'b', 'a', 'c'}




# 19) Write a programme to count
def char_count():
    text = "apple banana mango grape"
    words = text.split()
    for word in words:
        ch = input(f"enter word to search in {word} (or q to quit: ) ").strip().lower()
        if ch == 'q':
            print("Exiting...")
            return
        if len(ch)!=1:
            print(" enter correct word ")
            continue

        count = word.count(ch)
        print(f"{word} {ch} {count}\n")

    # 🔹 Part 2: Most frequent character in full string
    clean_text = text.replace(" ", "").lower()
    freq = Counter(clean_text)

    char, count = freq.most_common(1)[0]

    print(f"Most frequent character in full string: '{char}' with count = {count}")

char_count()
#20) Reverse each word individually but keep the word order same

sentence = "Welcome to Python 3.6"

# 1st way:
# One liner - List Comprehension
result = " ".join([word[::-1] for word in sentence.split()])

print(result)  # emocleW ot nohtyP 6.3

# 2nd way:
# Step 1 - Split into words
words = sentence.split()
print(words)  # ['Welcome', 'to', 'Python', '3.6']

# Step 2 - Reverse each word
reversed_words = [word[::-1] for word in words]
print(reversed_words)  # ['emocleW', 'ot', 'nohtyP', '6.3']

# Step 3 - Join back
result = " ".join(reversed_words)
print(result)  # emocleW ot nohtyP 6.3


#21 ) Reverse String — Keep Numbers & Special Chars in Place

def reverse_letters_only(s):
    # Step 1: Extract only letters
    letters = [c for c in s if c.isalpha()]

    # Step 2: Reverse the letters
    letters.reverse()

    # Step 3: Put letters back, keep others in place
    result = []
    letter_index = 0

    for char in s:
        if char.isalpha():
            result.append(letters[letter_index])
            letter_index += 1
        else:
            result.append(char)  # number/special stays

    return "".join(result)


# Test
print(reverse_letters_only("a1b2c3d"))
# d1c2b3a

print(reverse_letters_only("Welcome to Python 3.6"))
# nohtyPo te mocleW 3.6

#22) write a function to add two list using class

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
n1 = 10
n2 = 20


class listOperation:

    def __init__(self, list1, list2, n1, n2):
        self.list1 = list1
        self.list2 = list2
        self.n1 = n1
        self.n2 = n2

    def process_list(self):
        self.list1.append(self.n1)
        self.list2.append(self.n2)
        return [a + b for a, b in zip(self.list1, self.list2)]


obj = listOperation(list1, list2, n1, n2)

print(obj.process_list())


#23)write a program for finding non repeating charactor
from collections import Counter
count = Counter(s)
for ch in s:
    if count[ch]==1:
        print(ch)
        break

#24) longest substring o/p as string
def longest_substring(s):

    char_set = set()
    left = 0

    max_len = 0
    start = 0

    for right in range(len(s)):

        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])

        if right - left + 1 > max_len:
            max_len = right - left + 1
            start = left

    return s[start:start + max_len]


print(longest_substring("abcabcbb"))

#25)longest prefix
words = ["Flight", "Flow", "Florida", "Flower", "Floor", "Flour"]

def longest_prefix(words):
    if not words:          # Edge case: empty list
        return ""
    result = ""

    for char in zip(*words):        # Group characters column-wise
        if len(set(char)) == 1:     # All same character at this position?
            result += char[0]       # Yes → add to result
        else:
            break                   # No → stop here

    return result

print(longest_prefix(words))        # Output: Fl

#27) longest subfix
words = ["testing", "running", "playing", "string"]

def longest_common_suffix_zip(words):
    if not words:           # Edge case: empty list
        return ""

    result = ""

    # zip from the END of each word using reversed slicing
    for char in zip(*[w[::-1] for w in words]):
        if len(set(char)) == 1:             # All same character at this position?
            result += char[0]               # Yes → add to result
        else:
            break                           # No → stop here

    # Reverse the collected suffix characters
    return result[::-1]

print(longest_common_suffix_zip(words))  # Output: ing