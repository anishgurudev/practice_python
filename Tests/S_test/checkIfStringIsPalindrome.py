#Logic: Python's [::-1] reverses a string in one step. Compare it with the origin

# text = input("Enter a text :  ")
text = "A man , a plan, a canal: Panama"

def is_palindrome(string):
    string=string.lower()
    return string == string[::-1]   # True if original == reversed
print(is_palindrome(text))

def is_palindrome_sentence(string):
    # Keep only letters/digits, ignore spaces & punctuation
    cleaned="".join(char.lower() for char in string if char.isalnum())
    return cleaned == cleaned[::-1]   # True if original == reversed

print(is_palindrome_sentence(text))