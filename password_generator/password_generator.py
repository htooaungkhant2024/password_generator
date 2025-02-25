import random
import string

password_length = int(input("Enter your password_length :"))

char = string.ascii_letters
char += string.digits
char += string.punctuation

password = ""

for i in range(password_length):
    password += random.choice(char)

print("Your random password is:", password)