#Logic: split() with no argument splits on any whitespace(spaces, tabs, newlines)
# and removes empty strings.
# Then join() puts the words back together


string = ("Hello     world  \n Python")
# Step 1: split() → breaks on any whitespace
string_parts= string.split()
print(string_parts)
# Step 2: join() → merge with no separator
string = "".join(string_parts)
print(string)

#one liner solution
print("".join(string.split()))


