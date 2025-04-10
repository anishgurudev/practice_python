# 1) It should be able to accept a card number from the user. For this project, you can assume that the number will be entered as a single string
# of characters (i.e. there won't be any spaces between the numbers). However, you should be able to accept a card number with spaces at the start or end of the string.
card_number = list(input("Please Enter you card 16 digit card number: ").strip())
# If you want to challenge yourself, you should try to be more versatile with regards to the format that you accept card numbers in.
# You may want to turn the user's input into a list of numbers, as that will make it easier to work with.
# 2) The program should validate that card number using
# the Luhn algorithm described above. You should implement this algorithm yourself.
#striping the last no
striped_no = card_number.pop()
print(striped_no)
print(card_number)
#Reverse the remaining digits
card_number.reverse()
print(card_number)

#Double digits at even indices
pocessedCardNo = []
index = 0

for index,number in enumerate(card_number):
    if index % 2 == 0:
        doubled_digit = int(number)*2
        if doubled_digit >9:
            # Subtract 9 if over 9
            doubled_digit= doubled_digit-9
        pocessedCardNo.append(doubled_digit)
        print("even")
    else:
        pocessedCardNo.append(int(number))
        print("odd")
#sum these digits and add the checking digit
print(pocessedCardNo)
sum = sum(pocessedCardNo) + int(striped_no)
print(sum)
#divide by 10 is reminder is zero then card is valid
if sum % 10 ==0:
    print(f"your card {card_number.reverse()} is valid card!")
else:
    print(f"your card {card_number.reverse()} is invalid card!")

