print("-----")

print("Welcome to Map & Cheese! Been around since 2021")
print("Visit our website -> www.mapandcheese.com")
print("Our business hours are at the bottom of the page")

print("-----")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(f"Full name: {first_name} {last_name}")
correct_name = input("Is your name entered correctly? (yes/no) ")

if correct_name != 'yes':
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    print(f"Updated full name: {first_name} {last_name}")

age = int(input("Enter your age: "))
print(f"Your age: {age}")
correct_age = input("Is your age entered correctly? (yes/no) ")
if correct_age != 'yes':
    age = int(input("Enter your age: "))
    print(f"Updated age: {age}")


phone_number = input("Enter your phone number: ")
print(f"You entered {phone_number} for your phone number")
correct_phone_number = input("Is your phone number entered correctly? (yes/no) ")
if correct_phone_number != 'yes':
    phone_number = input("Enter your phone number: ")
    print(f"Your updated phone number is {phone_number}")