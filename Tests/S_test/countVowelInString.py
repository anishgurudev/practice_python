# Using set() (Fastest Lookup ⚡)
# Logic: Store vowels in a set for O(1) lookup speed. This is the same set() concept from our previous example!
from collections import Counter

text = "Automation Testing"


def count_vowel(words):
    vowels= {'a','e','i','o','u'}   # set → O(1) lookup
    count = 0

    for char in words.lower().strip():
        if char in vowels:   # Instant hash-based check
            count+=1

    return count


print(count_vowel(text))

def count_vowel_generator(word):
    return sum(1 for char in word.lower() if char in "aeiou")

print(count_vowel_generator(text))

def count_each_vowel_counter(word):
    vowels = "aeiou"
    freq = Counter(char for char in word.lower() if char in vowels)
    return dict(freq)
print(count_each_vowel_counter(text))  # Output: {'e': 3, 'o': 2, 'a': 1, 'u': 1, 'i': 1}

def count_vowels(s):
    vowels= "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

print(count_vowels(text))