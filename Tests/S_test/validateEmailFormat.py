# What Makes a Valid Email?
# A valid email has 3 parts:
#      rahul.dev@gmail.com
#     ─────────  ─────  ───
#     local part   domain  extension
# Local part: Letters, numbers, . _ % + -
# @ symbol: Exactly ONE @
# Domain: Letters, numbers, -
# Extension: .com, .org, .in etc. (2+ characters)

#| Piece             | Meaning                                           |
# | ----------------- | ------------------------------------------------- |
# | ^                 | Start of string                                   |
# | [a-zA-Z0-9._%+-]+ | Local part — letters, digits, ._%+- (1 or more)   |
# | @                 | Literal @ symbol (exactly once)                   |
# | [a-zA-Z0-9.-]+    | Domain name — letters, digits, . -                |
# | \\.               | Literal dot (escaped with \\)                     |
# | [a-zA-Z]{2,}      | Extension — letters only, min 2 chars (.com, .in) |
# | $                 | End of string                                     |
import re

email = "rahul.dev@y0ah.koo"

def is_email_valid(mail):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern,mail))

print(is_email_valid(email))

def email_valid(mail):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,}$'
    if re.fullmatch(pattern, mail):
        return True
    return False

print(email_valid(email))
