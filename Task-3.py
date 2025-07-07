import string
import random

length = int(input("Enter the designed password length:"))
all_characters = string.ascii_letters + string.digits + string.punctuation
password = ".join(random.choice(all_characters) for_in range(length))
print("Generated Password: , password")