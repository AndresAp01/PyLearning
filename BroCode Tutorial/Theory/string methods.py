#name = input("Enter your full name: ")
#phone_number = input("Enter your phone number: ")

#result = len(name)
#result = name.find(" ")
#result = name.rfind("a")
#name = name.capitalize()
#name = name.upper()
#name = name.lower()
#result = name.isdigit()
#result = name.isalpha()
#result = phone_number.count("-")
#result = phone_number.replace("-", " ")

#print(result)

#Excercise!
#validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Hello. Please assign a username, it must be 12 characters max, no spaces, no digits. Enter your username: ")

if len(username) > 12:
    print("Your username cannot be more than 12 characters.")
elif not username.find(" ") == -1:
    print("Your username can't contain spaces.")
elif not username.isalpha():
    print("Your username must contain only letters.")
else:
    print(f"Welcome {username}")

