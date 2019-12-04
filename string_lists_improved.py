#Practice Program
#Ask the user for a string and print out whether this string is a palindrome or not.

user_input = input("Please provide a string to determine if it is a palindrome: ")

rev = user_input[::-1]

if user_input == rev:
    print("This is a palindrome")
else:
    print("This is not a palindrome")