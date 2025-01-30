#Day 2: 30 Days of Python programming
#Variables in Python

first_name = "Andres"
last_name = "Acuna"
full_name = first_name + " " + last_name
country = "Costa Rica"
city = "Cartago"
age = 23
year = 2025
is_male = True
is_light_on = False

university, phone_number, number_pet = "TEC", "84960390", "3"

#Exercises: Level 2

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_male))

print(len(first_name))
print(len(first_name) - len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_one
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print(total, diff, product, division, remainder, exp, floor_division)

#12 The radius of a circle is 30 meters
#Area = pi * r^2
radius_of_circle = 30
area_of_circle = (3.14 * (radius_of_circle**2))
print(area_of_circle)

circum_of_circle = 3.14 * radius_of_circle * 2
print(circum_of_circle)

radius = float(input("Enter radius of the circle: "))
Area = (3.14 * (radius**2))
print("The area of the circle is: " + str(Area))

user_first_name = str(input("Enter first name: "))
user_last_name = str(input("Enter last name: "))
user_age = int(input("Enter age: "))

print(user_first_name, user_last_name, user_age)
