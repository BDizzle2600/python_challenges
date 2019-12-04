#Practice Program
#Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user

user_number = input("This program determines odd or even.  Please provide a number: ")

def odd_even(number):
    if float(number) % 2 != 0:
        message = "Your number was odd"
    else:
        message = "Your number was even"
    return message

print(odd_even(user_number))