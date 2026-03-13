from openpyxl.styles.builtins import total

cardNo= input("enter Credit card no: ").replace(" ","")

listCardNo= list(str(cardNo))
print(listCardNo)
#Remove the last digit
lastremoved=listCardNo.pop()
print(lastremoved)
print(listCardNo)
#Reverse the remaining digits
listCardNo.reverse()
print(listCardNo)
#Double digits at even indices
index = 0
processed_digits = []

for digit in listCardNo:
    if index % 2 == 0:
        double_digit = int(digit) * 2
        #subtract 9 if any result is greater the 9
        if double_digit>9:
            double_digit= double_digit-9
        print(f"even index at position {index} now {double_digit}")
        processed_digits.append(double_digit)
    else:
        print(f"odd index at position {index} now {digit}")
        processed_digits.append(digit)
    index =index+1
print(processed_digits)

total= int(lastremoved)
for digit in processed_digits:
    total = total + int(digit)
print(total)

# Verify that the sum of the digits is divisible by 10
if total%10 ==0:
    print("valid")
else:
    print("invalid")