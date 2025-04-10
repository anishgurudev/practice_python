# validate credit card using Luhn algorithm,
card_number = list(input("Please enter a card number: ").strip())
# print(card_number)

# Remove the last digit from the card number
last_digit = card_number.pop()
# print(last_digit)

# Reverse the order of the remaining numbers
card_number.reverse()
# print(card_number)

proceed_digit = []
for index, digit in enumerate(card_number):
    if index % 2 == 0:
        doubled_digit = int(digit) * 2
        if doubled_digit > 9:        # Subtract 9 from any results that are greater than 9
            doubled_digit = doubled_digit - 9
        proceed_digit.append(doubled_digit)
    else:
        proceed_digit.append(int(digit))

# print(proceed_digit)
total = int(last_digit) + sum(proceed_digit)
# print(total)

if total % 10 == 0:
    print(f"Valid card no!")
else:
    print(f"Invalid card no!")

