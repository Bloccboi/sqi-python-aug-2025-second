# is_raining = True

# if is_raining:
#     print("Carry an umbrella")
# else:
#     print("No need for an umbrella")



# num1 = 2
# num2 = 2

# if num1 > num2:
#     print("num1 is greater")
# else:
#     print("num2 is greater or equal to num1")


# Ask the user for a number
# Print "It is even" if the number is even
# otherwise, print "it is odd"

# number = int(input("Enter a number: "))
# is_even = number % 2 == 0
# if is_even:
#     print("It is even")
# else:
#     print("It is odd")


# num1 = 12
# num2 = 102

# if num1 > num2:
#     print("num1 is greater")
# elif num1 < num2:
#     print("num2 is greater")
# else:
#     print("num1 and num2 are equal")

 

# word = input("Enter a word: ")
# if word.lower().startswith("a"):
#     print(f"The word '{word}' starts with a")
# else:
#     print(f"The word '{word}' does not start with a")


# word = input("Enter a word: ").strip()

# if word[0].lower() == "a":
#     print(f"The word '{word}' starts with a")
# else:
#     print(f"The word '{word}' does not start with a")


# Ask the user for a sentence
# if all the characters are lowercase, print "Everything is in lowercase"
# otherwise, print "Not everything is in lowercase"


# sentence = input("Enter a sentence: ").strip()
# if sentence.islower():
#     print("Everything is in lowercase")
# else:
#     print("Not everything is in lowercase")


# If the temp is between 0 and 30, "It is cold outside"
# If the temp is between 31 and 59 "It is warm outside"
# If the temp is greater than or equal to 60, "It is hot outside"

# temp = int(input("Enter the temperature: "))

# if temp < 0:
#     print("It is freezing")
# elif 0 <= temp <= 30:
#     print("It is cold outside")
# elif 31 <= temp <= 100:
#     print("It is warm outside")
# else:
#     print("Invalid temp entered")
#     # raise ValueError("Invalid temp entered")


# Ask the user for their score and tell them their grade
# If their score is less than 30 and greater than or eqaul to 0, print "F"
# if their score is equal to or greater than 30 and less than or equal to 59, print "C"
# If their score is 60 or greater than 60 and less than or equal to 100, print "A"

# score = int(input("Enter your score: "))

# if 0 <= score < 30:
#     print("F")
# elif 30 <= score <= 59:
#     print("C")
# elif 60 <= score <= 100:
#     print("A")
# else:
#     print("Invalid score")




# husband = None
# husband = "James"


# if husband is None:
#     print("No husband")
# else:
#     print("Has husband")

# husband = "Ayo"
# husband = ""

# if husband:
#     print("Husband has a name")
# else:
#     print("Husband does not have a name")


# name = input("What is your name? ").strip()
# name = input("What is your name? ")

# if name:
#     print(f"Good morning, {name}!")
# else:
#     print(f"Good morning, Anonymous!")


# name = input("What is your name? ").strip()

# if name: print(f"Good morning, {name}!")
# else: print(f"Good morning, Anonymous!")


# is_male = False
# print("He" if is_male else "She")
# print("He") if is_male else print("She")


# is_male = False
# pronoun = "He" if is_male else "She"
# print(pronoun)


# is_male = False

# if is_male:
#     print("He")
# else:
#     print("She")


# is_male = False
# if is_male:
#     pronoun = "He"
# else:
#     pronoun = "She"

# print(pronoun)


# has_umbrella = True
# has_raincoat = True

# # If they have an umbrella or they have a raincoat, print "You are protected from the rain"
# # If the person has an umbrella and has a raincoat, print "You have double protection from the rain"
# # If they have none, print "You are NOT protected from the rain"

# if has_umbrella and has_raincoat:
#     print("You have double protection from the rain")
# elif has_umbrella or has_raincoat:
#     print("You are protected from the rain")
# else:
#     print('you are NOT protected form the rain')

# has_umbrella = False
# has_raincoat = True


# if has_umbrella:
#     print("You are protected from the rain")
# elif has_raincoat:
#     print("You are protected from the rain")
# elif has_umbrella and has_raincoat:
#     print("You have double protection from the rain")
# else:
#     print("You are NOT protected form the rain")



# name = input("What is your name? ").strip()

# if not name:
#     print("You must enter a name")


# students = ["Praise", "Maryam", "John", "Ayomide"]
# students = [""]

# if students:
#     print("there are students in the class")
# else:
#     print("there are no students in the class")



# is_male = False
# age = 21


# if is_male:
#     if age >= 18:
#         print("You can vote")
#     else:
#         print("You cannot vote")
# else:
#     print("Women do not have the right to vote")
    


# import random

# genders = [
#     "Male",
#     "Female",
#     "Transgender Male",
#     "Transgender Female",
#     "Non-binary",
#     "Genderqueer",
#     "Genderfluid",
#     "Agender",
#     "Bigender",
#     "Two-Spirit",
#     "Demiboy",
#     "Demigirl",
#     "Androgynous",
#     "Intersex"
# ]

# gender = random.choice(genders)

# print(gender)

# age = 12


# if age < 18:
#     if gender == "Male":
#         print("You are a young boy.")
#     elif gender == "Female":
#         print("You are a young girl.")
#     elif gender == "Non-binary":
#         print("You are a young non-binary person.")
#     else:
#         print(f"You are young and identify as {gender}.")
# elif 18 <= age <= 40:
#     if gender == "Male":
#         print("You are an adult man.")
#     elif gender == "Female":
#         print("You are an adult woman.")
#     elif gender == "Non-binary":
#         print("You are an adult non-binary person.")
#     else:
#         print(f"You are an adult and identify as {gender}.")
# else:  # age > 40
#     if gender == "Male":
#         print("You are a mature man.")
#     elif gender == "Female":
#         print("You are a mature woman.")
#     elif gender == "Non-binary":
#         print("You are a mature non-binary person.")
#     else:
#         print(f"You are mature and identify as {gender}.")



# is_female = True

# if is_female:
#     # I will write something here
#     pass
# print("End of file")
        


# You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".

# mode = input("Enter a mode, either manual, automatic or off: ").strip().lower()

# if mode == "manual":
#     print("Manaul mode activated")
# elif mode == "automatic":
#     print("Automatic mode activated")
# elif mode == "off":
#     print("System is off")
# else:
#     print("Invalid mode")



# mode = input("Enter a mode, either manual, automatic or off: ").strip().lower()

# if mode == "manual" or mode == "automatic":
#     print(f"{mode} mode activated")
# elif mode == "off":
#     print("System is off")
# else:
#     print("Invalid mode")


# Collect word1, word2 and word3 as comma separated inputs from the user

# hi, hello, hey


# word1, word2, word3 = input("Enter three words separated by commas: ").strip().split(", ")

# print(word1)
# print(word2)
# print(word3)


# -------------------------------ASSIGNMENT CORRECTION-------------------------------

# 1. Collect two numbers as input from the user and assign as variables, a and b, write an if 
# statement that prints "a and b are both positive" if both a and b are positive, prints 
# "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# neither is positive.

# a = int(input("Enter the first number: "))  # 5
# b = int(input("Enter the second number: "))  # -4

# if a > 0 and b > 0:
#     print("Both are positive")
# elif a > 0 or b > 0:
#     print("Only one is positive")
# else:
#     print("Neither is positive")


# 2. Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.

# x, y, z = input("Enter three numbers separated by commas: ").split(",")
# x, y, z = int(x), int(y), int(z)



# 3. Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".

# palindrome = input("Enter some text: ").strip().replace(" ", "")

# if palindrome == palindrome[::-1]:
#     print("Is a palindrome")
# else:
#     print("Not a palindrome")



# 4. You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. Otherwise, print "All different" or "All same" accordingly.

# x = input("Enter the value of x: ")
# y = input("Enter the value of y: ")
# z = input("Enter the value of z: ")

# if x == y == z:
#     print("All same")
# elif x == y or y == z or x == z:
#     print("Two are equal")
# else:
#     print("All different")


# 5. Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements to check if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".

# angle1 = float(input("Enter the value of angle 1: "))
# angle2 = float(input("Enter the value of angle 2: "))
# angle3 = float(input("Enter the value of angle 3: "))


# if (angle1 > 0 and angle2 > 0 and angle3 > 0) and (angle1 + angle2 + angle3 == 180):
#     print("Valid triangle") 
# else:
#     print("Invalid triangle") 

# 6. You have a single character variable `ch` supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that the input is a single alphabet character.


# ch = input("Enter a single alphabet character: ").strip().lower()
# if ch in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")


# You have a single character variable `ch` supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise.

# ch = input("Enter a single alphabet character: ").strip().lower()
# if len(ch) != 1:
#     print("Enter a single alphabet character")
# elif ch in "aeiou":
#     print("Vowel")
# else:
#     print("Consonant")

# married = None

# if married is not None

# married = "yes"
# married = "no"

# if married == "yes"

# ch = input("Enter a single alphabet character: ").strip().lower()
# if not ch.isalpha() or len(ch) != 1:
#     print("Enter a single alphabet character")
# else:
#     if ch in "aeiou":
#         print("Vowel")
#     else:
#         print("Consonant")


# returning early

# def vowel_or_consonant():
#     ch = input("Enter a single alphabet character: ").strip().lower()
#     if not ch.isalpha():
#         return "Enter an alphabet"
    
#     if len(ch) != 1:
#         return "Enter a single character"

#     if ch in "aeiou":
#         print("Vowel")
#     else:
#         print("Consonant")



# 7. Given a comma separated string input from the user of three colors color1, color2, and color3, write an if statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".


# INTERPRETATION 1
# color1, color2, color3 = input("Enter three colors separated by commas: ").split(",")
# color1, color2, color3 = color1.strip().lower(), color2.strip().lower(), color3.strip().lower()

# primary_colors = ("red", "blue", "yellow")

# if color1 in primary_colors and color2 in primary_colors and color3 in primary_colors:
#     print("All primary colors")
# else:
#     print("Not all primary colors")


# INTERPRETATION 2
# color1, color2, color3 = input("Enter three colors separated by commas: ").split(",")
# color1, color2, color3 = color1.strip().lower(), color2.strip().lower(), color3.strip().lower()

# primary_colors = {"red", "blue", "yellow"}
# colors = {color1, color2, color3}

# if colors == primary_colors:
#     print("All primary colors")
# else:
#     print("Not all primary colors")


# 8. You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".

# 9. Given a string `message` entered by the user, use if statements to check if the message contains any of the words "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".

# message = input("Enter a message: ").lower()

# if "urgent" in message or "immediate" in message or "important" in message:
#     print('High priority message')
# else:
#     print("Normal message")


# 10. You have two variables, status1 and status2, provided through user input, each of 
# which can be "active", “inactive", or "pending". Write an if statement to print 
# "Both active" if both statuses are "active", "One active" if exactly one is "active",
# and "None active" if neither is "active".


# status1 = input("Enter status 1, either active, inactive or pending: ").strip().lower()
# status2 = input("Enter status 2, either active, inactive or pending: ").strip().lower()

# valid_statuses = ["active", "inactive", "pending"]

# if status1 not in valid_statuses or status2 not in valid_statuses:
#     print("status 1 and status2 must be either active, pending or inactive")
# elif status1 == "active" and status2 == "active":
#     print("Both active")
# elif status1 == "active" or status2 == "active":
#     print("One active")
# else:
#     print("None active")


# 11. Given a string `filename` supplied by the user, write an if statement to check if the
# filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
# print "Not an image file".

# filename = input("Enter a filename: ").strip().lower()

# if filename.endswith((".jpg", ".png", ".gif")):
# # if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".gif"):
#     print("Image file")
# else:
#     print("Not an image file")


# 12. You have a variable `access_level` provided through user input which can be "admin",
# "user", or "guest". Write an if statement that prints "Full access" if access_level is
# "admin", "Limited access" if it is "user", and "No access" if it is "guest".

# access_level = input("Enter your access level: ").strip().lower()
# if access_level == "admin":
#     print("Full access")
# elif access_level == "user":
#     print("Limited access")
# elif access_level == "guest":
#     print("Limited access")
# else:
#     print("No access")


# 13. 	Given a string `email` collected from the user, write an if statement to check if the
# email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise
# print "Invalid email".

# email = input("Enter an email address: ").strip().lower()

# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")


# email = input("Enter an email address: ").strip().lower()

# # if "@" and ("." in email):  # wrong
# # if "@" and "." in email:  # gotcha
#     print("Valid email")
# else:
#     print("Invalid email")


# 14. You have a variable `day` provided by user input which can be any day of the week 
# (e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
# day is "Saturday" or "Sunday", and "Weekday" if it is any other day.

# day = input("Enter a day of the week: ").strip().capitalize()
# weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# weekend = ["Saturday", "Sunday"]

# if day in weekend:
#     print("Weekend")
# elif day in weekday:
#     print("Weekday")
# else:
#     print("Invalid Day")

# 15. Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
# input from the user and prints the greatest number. Use conditional statements
# to determine which number is the greatest. Bonus point if you can do it without `else` 
# statements.

# num1, num2, num3 = input("Enter three numbers separated by commas: ").split(",")
# num1, num2, num3 = int(num1), int(num2), int(num3)

# if num1 >= num2 and num1 >= num3:
#     print(f"{num1} is the greatest")
# elif num2 >= num1 and num2 >= num3:
#     print(f"{num2} is the greatest")
# else:
#     print(f"{num3} is the greatest")

# num1, num2, num3 = input("Enter three numbers separated by commas: ").split(",")
# num1, num2, num3 = int(num1), int(num2), int(num3)


# greatest = num1

# if num2 > greatest:
#     greatest = num2

# if num3 > greatest:
#     greatest = num3

# print(f"{greatest} is the greatest")

# -------------------------------ASSIGNMENT CORRECTION-------------------------------



# -------------------------------ASSIGNMENT 27th August, 2025-------------------------------
# Exercise 1
# An amusement park ride has these rules:
# - Must be at least 120 cm tall to ride.
# - If under 120 cm but with an adult, still allowed.
# - Otherwise, not allowed.
#
# Example input/output executions:
#
# Enter height: 130
# With adult? no
# Output: Allowed
#
# Enter height: 110
# With adult? yes
# Output: Allowed
#
# Enter height: 110
# With adult? no
# Output: Not allowed
#
# Enter height: 119
# With adult? yes
# Output: Allowed
#
# Enter height: 100
# With adult? no
# Output: Not allowed
#
# Enter height: 150
# With adult? no
# Output: Allowed


# height = int(input("Enter height: "))
# with_adult = input("With adult? : ").lower()
# if height >= 120 or (height < 120 and with_adult == "yes"):
#     print("Allowed")
# else:
#     print("Not allowed")



# Exercise 2
# An exam grading system with retake rule:
# The user enters exam score and retake status ("yes" or "no").
# - If score is at least 50, print "Pass".
# - If score is less than 50 but retake is "yes", print "Retake allowed".
# - If score is less than 50 and no retake, print "Fail".
#
# Example input/output executions:
#
# Enter score: 42
# Retake? yes
# Output: Retake allowed
#
# Enter score: 42
# Retake? no
# Output: Fail
#
# Enter score: 50
# Retake? no
# Output: Pass
#
# Enter score: 75
# Retake? yes
# Output: Pass
#
# Enter score: 10
# Retake? no
# Output: Fail

# score = int(input("Enter score: "))
# retake = input("Retake? (yes/no): ").lower()

# if score >= 50:
#     print("Pass")
# elif retake == "yes":
#     print("Retake allowed")
# else:
#     print("fail")


# Exercise 3
# A ride-hailing app calculates trip approval:
# The user enters distance (km) and wallet balance.
# Each km costs 200 units.
# - If wallet balance is enough for the trip, print "Trip confirmed".
# - If balance is less but at least half the cost, print "Add funds".
# - If less than half, print "Trip denied".
#
# Example input/output executions:
#
# Enter distance: 10
# Enter wallet balance: 800
# Output: Add funds
#
# Enter distance: 10
# Enter wallet balance: 2000
# Output: Trip confirmed
#
# Enter distance: 10
# Enter wallet balance: 1000
# Output: Trip confirmed
#
# Enter distance: 10
# Enter wallet balance: 400
# Output: Trip denied
#
# Enter distance: 5
# Enter wallet balance: 500
# Output: Trip confirmed



# Exercise 4
# An airport boarding system:
# The user enters boarding pass ("yes"/"no") and passport ("yes"/"no").
# - If both are "yes", print "Proceed to boarding".
# - If boarding pass is missing, print "No boarding pass".
# - If passport is missing, print "No passport".
# - If both missing, print "Denied entry".
#
# Example input/output executions:
#
# Boarding pass? no
# Passport? yes
# Output: No boarding pass
#
# Boarding pass? yes
# Passport? no
# Output: No passport
#
# Boarding pass? no
# Passport? no
# Output: Denied entry
#
# Boarding pass? yes
# Passport? yes
# Output: Proceed to boarding
#
# Boarding pass? no
# Passport? yes
# Output: No boarding pass


# -------------------------------ASSIGNMENT 27th August, 2025-------------------------------



# Print all the numbers from 3 to 27
i = 3
while i <= 27:
    print(i)
    i += 1



# Print all the numbers from 90 to 16

i = 90
while i >= 16:
    print(i)
    i -= 1
    


# Print all the even numbers from 8 to 24 ie 8, 10, 12, 14, 16, 20 , 22, 24  

i = 8
while i <= 24:
    print(i)
    i += 2

 
 
i = 8
while i <= 22:
    print(i)
    i += 1



i = 7
while i <= 36:
    if i % 5 == 0:  
        print(i)
    i += 1
    
    


# numbers = []
# i = 1
# while i <= 50:
#     numbers.append(str(i))
#     i += 1
# print(numbers)

# print(", ".join(numbers))

numbers = []
i = 60
while i < 70:
    numbers.append(i)
    i += 1

print(numbers)


numbers = []
i = 10
while i <= 20:
    if i != 15:  
        numbers.append(i)
    i += 1

print(numbers)