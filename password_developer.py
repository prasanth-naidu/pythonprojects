import random
import string
length = int(input("enter the length:"))
characters = string.ascii_letters + string.digits + string.punctuation
password = ""
for i in range(length):
    password += random.choice(characters)
print("generated password",password)