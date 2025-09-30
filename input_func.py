# name = input("What is your name?: ")
# print(f"Hello, {name}!")


# favorite_color
# Red is awesome!


# Ask the user to enter their location
# And ask them to enter their phone number

# Output:
# Location: SQI
# Phone Number: 09030556529

# location = input("Enter your location: ").strip()
# phone_number = input("Enter your phone number: ").strip()

# print(f"""Location: {location}
# Phone number: {phone_number}""")



# Ask the user for their first_name, last_name, email and phone number

# Output:

# Contact Information:
# Name: Winifred Igboama
# Email: winnie@gmail.com
# Phone: 09030556512


# first_name = input("Enter your first name: ").strip()
# last_name = input("Enter your last name: ").strip()
# email = input("Enter your email address: ").strip()
# phone_num = input("Enter your phone number: ").strip()


# print(f"""Contact Information:
# Name: {first_name} {last_name}
# Email: {email}
# Phone: {phone_num}""")


# john_favorite_num = input("John, enter your favorite number: ")

# benjamin_favorite_num = input("Benjamin, enter your favorite number: ")

# sum_of_their_nums = int(john_favorite_num) + int(benjamin_favorite_num)
# print("The sum of their favorite numbers is " + str(sum_of_their_nums))
# print(f"The sum of their favorite numbers is {sum_of_their_nums}")



# Ask the user for their age
# Tell them when they were born


# import datetime

# current_year = datetime.datetime.now().hour

# print(current_year)

# from datetime import datetime

# current_year = datetime.now().year

# age = input("How old are you now?: ")
# birth_year = current_year - int(age)
# print(f"You were born in {birth_year}")



# One has been done for you as an example:

# Sample Execution:
# Enter your name: David
# Enter the activity you did (e.g., running, cycling): Hiking
# Enter the duration of the activity (in minutes): 120
# Enter the calories burned: 850
#
# Fitness Activity:
# Name: David
# Activity: Hiking
# Duration: 120 minutes
# Calories Burned: 850 kcal
#
# Task:
# Write a Python program that works exactly like the sample above.
# The program should ask the user for their name, activity, duration, and calories burned,
# and then print the details in the same format.

# Solution
# name = input("Enter your name: ")
# activity = input("Enter the activity you did (e.g., running, cycling): ")
# duration = input("Enter the duration of the activity (in minutes): ")
# calories = input("Enter the calories burned: ")

# print("\nFitness Activity:")
# print(f"Name: {name}")
# print(f"Activity: {activity}")
# print(f"Duration: {duration} minutes")
# print(f"Calories Burned: {calories} kcal")


# NOW DO THESE:
# Exercise 1:
# Sample Execution:
# Enter your first name: Alice
# Enter your last name: Johnson
#
# Full Name: Alice Johnson
#
# Task:
# Write a Python program that asks the user for their first name and last name,
# then prints their full name in the format shown above.


# Exercise 2:
# Sample Execution:
# Enter the length of the rectangle: 8
# Enter the width of the rectangle: 5
#
# Area of the rectangle: 40
#
# Task:
# Write a Python program that calculates the area of a rectangle.
# The program should ask for length and width, then display the area.


# Exercise 3:
# Sample Execution:
# Enter the temperature in Celsius: 25
#
# Temperature in Fahrenheit: 77.0
#
# Task:
# Create a Python program that converts a temperature from Celsius to Fahrenheit.
# Formula: F = (C × 9/5) + 32


# Exercise 4:
# Sample Execution:
# Enter the number of apples: 4
# Enter the number of bananas: 6
#
# Total fruits: 10
#
# Task:
# Write a program that asks the user for the number of apples and bananas,
# then prints the total number of fruits.


# Exercise 5:
# Sample Execution:
# Enter your age: 30
#
# You will be 35 years old in 5 years.
#
# Task:
# Create a program that asks the user for their age,
# then calculates and prints how old they will be in 5 years.


# Exercise 6:
# Sample Execution:
# Enter the distance in kilometers: 10
#
# Distance in miles: 6.21371
#
# Task:
# Write a Python program that converts kilometers to miles.
# 1 kilometer = 0.621371 miles.


# Exercise 7:
# Sample Execution:
# Enter your favorite color: Blue
# Enter your favorite food: Pizza
#
# Your favorite color is Blue and your favorite food is Pizza.
#
# Task:
# Write a Python program that asks the user for their favorite color and food,
# then displays the message exactly like the example.


# Exercise 8:
# Sample Execution:
# Enter the price of an item: 50
# Enter the discount percentage: 20
#
# Price after discount: 40.0
#
# Task:
# Write a program that calculates the final price after a discount.
# Formula: final_price = price - (price × discount/100)


# Exercise 9:
# Sample Execution:
# Enter the number of hours worked: 40
# Enter your hourly rate: 15
#
# Weekly pay: 600
#
# Task:
# Write a program that calculates a worker's weekly pay
# based on hours worked and hourly rate.


# Exercise 10:
# Sample Execution:
# Enter your favorite movie: Inception
# Enter your favorite song: Bohemian Rhapsody
#
# Your favorite movie is Inception and your favorite song is Bohemian Rhapsody.
#
# Task:
# Create a Python program that asks the user for their favorite movie and song,
# then prints them in the same format as the example.



# password = input("Enter your password: ").strip()

# print(f"Your password is {password}")


# import string
# import datetime
# import getpass


# password = getpass.getpass("Enter your password: ")
# print(f"Your password is {password}")

# PSL - Python Standard Library


# ========================================MAD LIBS GAME 1========================================

# plural_noun_1 = input("Enter a plural noun: ").strip()
# person_in_room_last_name = input("Enter the last name of someone in the room: ").strip()
# adjective_1 = input("Enter an adjective: ").strip()
# noun_1 = input("Enter a noun: ").strip()
# noun_2 = input("Enter another noun: ").strip()
# part_of_the_body_1 = input("Enter a part of the body: ").strip()
# part_of_the_body_2 = input("Enter another part of the body: ").strip()
# plural_noun_2 = input("Enter a plural noun: ").strip()
# noun_3 = input("Enter a noun: ").strip()
# noun_4 = input("Enter another noun: ").strip()
# exclamation = input("Enter an exclamation: ").strip()
# noun_5 = input("Enter a noun: ").strip()
# noun_6 = input("Enter another noun: ").strip()
# noun_7 = input("Enter another noun: ").strip()
# verb_1 = input("Enter a verb: ").strip()
# noun_8 = input("Enter a noun: ").strip()
# adjective_2 = input("Enter an adjective: ").strip()
# noun_9 = input("Enter a noun: ").strip()


# story = f"""A one-act play to be perfromed by two {plural_noun_1} in this room.
# PATIENT: Thank you so very much for seeing me, Doctor {person_in_room_last_name}, on such {adjective_1} notice.
# DENTIST: What is your problem, young {noun_1}?
# PATIENT: I have a pain in my upper {noun_2} which is giving me a severe {part_of_the_body_1} ache.
# DENTIST: Let me take a look. Open your {part_of_the_body_2} wide. Good. Now I am going to tap your {plural_noun_2} with my {noun_3}.
# PATIENT: Shouldn't you give me a/an {noun_4} killer?
# DENTIST: It's not necessary yet. {exclamation}! I think I see a/an {noun_5} in your upper {noun_6}.
# PATIENT: Are you going to pull my {noun_7} out? 
# DENTIST: No. I'm going to {verb_1} your tooth and put in a temporary {noun_8}.
# PATIENT: When do I come back for the {adjective_2} filling?
# DENTIST: A day after I cash your {noun_9}
# """

# print(story)

# ========================================MAD LIBS GAME 2========================================
# person_in_room_name_1 = input("Enter the name of someone: ").strip()
# number_1= input("Enter a  number: ").strip()
# adjective_1 = input("Enter an adjective: ").strip()
# color = input("Enter a color: ").strip()
# noun_1 = input("Enter a noun: ").strip()
# plural = input("Enter a  type of food (plural): ").strip()
# noun_2= input("Enter a noun: ").strip()
# verb_1= input("Enter a verb ending in 'ing': ").strip()
# clothing = input("Enter an article of clothing: ").strip()
# adjective_2 = input("Enter an adjective: ").strip()
# celebrity = input("Enter a celebrity's name: ").strip()
# number_2 = input("Enter a number: ").strip()
# person_in_room_name_2= input("Enter the name  of someone: ").strip()
# noun_3= input("Enter a noun: ").strip()
# person_in_room_name_3= input("Enter the name of someone: ").strip()
# occupation= input("Enter an occupation: ").strip()


# story = f"""My name is {person_in_room_name_1} and I am {number_1} years old. If I were President,I'd do a whole bunch of{adjective_1} things:
# 1. I would drive the biggest {color} car in the country. And that car would go faster than any other {noun_1} in the world!
# 2. Everyone would eat peppernoni  {plural} for dinner.
# 3. I would live in the statue of {noun_2} and build a {verb_1} pool at her feet.
# 4. I would wear a/an {clothing} on my head, and everyone would say I look {adjective_2} like {celebrity}
# 5. School would be open only {number_2} days a year.
# 6. I would give my friends the best jobs. I would nominate {person_in_room_name_2} to be secretary of (the) {noun_3} and {person_in_room_name_3} could be vice {occupation}"""


# print(story)

# ========================================MAD LIBS GAME 3========================================
term_endearment = input("Enter a term of endearment: ")
first_name = input("Enter a first name: ")
full_name = input("Enter a first and last name: ")
place = input("Enter a place: ")
day_of_week = input("Enter a day of the week: ")
adjective = input("Enter an adjective: ")
color = input("Enter a color: ")
clothing = input("Enter an item of clothing: ")
number = input("Enter a number: ")
verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")
verb3 = input("Enter another verb: ")
verb4 = input("Enter one more verb: ")


story = f"""
Hey, {term_endearment}. It's me. What's up? You know, {first_name}. 
{full_name}. From the {place}. Two {day_of_week}s ago. 
I was the {adjective} guy in the {color} parachute {clothing}.  

I paid the bus boy {number} dollars to {verb1} me your information.  
I was wondering if maybe you'd like to {verb2} out with me.  
Please don't call the {verb3} department.  

Alright, I'll {verb4}.  
So, that's a no, right?
"""