# find the number of count for each alphabet.

from collections import Counter

letters = "abcdabcdABCD"

#string to collection of character
char_list = list(letters )

# Count each character
count_result = Counter(char_list)

# Print result
for letter, count in count_result.items():
    print(f"{letter} = {count}")

print("new code")

#2nd way

letters = "abcdabcdABCD"
char_list = list(letters )
print(char_list)

count_result = {}

for letter in char_list:
    if letter in count_result:
        count_result[letter] += 1
    else:
        count_result[letter] = 1

# Print result
for letter, count in count_result.items():
    print(f"{letter} = {count}")
#-------------------------





