import string
import random

#store all possible characters in a string
characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation

#ask user how long they want their password
password_length = int(input('Please enter length of password: '))
password = ''

for i in range(password_length):
    random_num = random.randint(0, len(characters) - 1)
    password += characters[random_num]

print('Here is your password: ' + password)