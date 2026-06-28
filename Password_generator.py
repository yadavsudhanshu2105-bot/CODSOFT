import random
import string

print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length as per your choice: "))

letters = string.ascii_letters
numbers = string.digits
symbols = "@#$%&*!"

all_characters = letters + numbers + symbols

password = ""

for i in range(length):
    password += random.choice(all_characters)

print("\nGenerated Password:")
print(password)
