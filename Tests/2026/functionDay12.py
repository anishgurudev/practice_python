#function:They allow us to cut down on repeating potentially long and complicated code for operations we want to perform multiple times.
#for finding first 10 even no
# for number in range(1, 11):
#     print(number * 2)

# def get_even_numbers():
#     for number in range(2,21,2):
#         print(number)


# get_even_numbers()

def get_even_numbers(number):
    for no in range(1,number+1):
        print(no*2)

get_even_numbers(5)

len([1, 3, 5])  # 3
# len()  # Error!

def x_print(requested_output,quantity):
    for x in range(quantity):
        print(requested_output)


x_print("Hello!",5)
# x_print(5,"Hi") #
x_print(quantity=5,requested_output="hi")