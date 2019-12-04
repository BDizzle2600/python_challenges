#Practice Program
#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

user_input = input("Please provide a number: ")

def divisor(number):
    a = []
    x = number
    while x > 0:
        if number % x == 0:
            a.append(x)
        x -= 1
    return(a)

print(divisor(int(user_input)))