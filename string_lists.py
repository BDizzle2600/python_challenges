#Practice Program
#Ask the user for a string and print out whether this string is a palindrome or not.

user_input = input("Please provide a string to determine if it is a palindrome: ")

rev = []
chars = len(user_input) * -1
x = -1
y = 0

while x >= chars:
    rev.append(user_input[x])
    x -= 1

while y < len(user_input):
    if user_input[y] == rev[y]:
        msg = "This is a palindrome"
        y += 1
        continue
    else:
        msg = "This is not a palindrome"
        break
print(msg)