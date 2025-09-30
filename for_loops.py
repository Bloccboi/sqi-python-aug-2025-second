# hobbies = ["singing", "dancing", "reading", "sleeping", "coding", "cooking"]
# i = 0

# while i < len(hobbies):  # i is the iterator or loop control variable
#     hobby = hobbies[i]
#     print(hobbies)
#     i += 1


# hobbies = ["singing", "dancing", "reading", "sleeping", "coding", "cooking"]

# for hobby in hobbies:
#     print(hobby)


# Create a tuple containing the following streaming services in order:
# Netflix, Amazon Prime, Hulu, Disney Plus, UEFA TV, AppleTV


# streaming_services = ("Netflix", "Amazon Prime", "Hulu", "Disney Plus", "UEFA TV", "AppleTV")

# for streaming_service in streaming_services:
#     print(streaming_service)

# Loop through each tuple and print each streaming service.

# for my_hobby in hobbies:
#     print(my_hobby)

# for hobbies in hobbies:
#     print(hobbies)

# print(hobbies)

# for _ in hobbies:
#     print("Hobby")


# the while loops give you more control over the execution of the code
# the for loops are for simply looping through every single item in the iterable


# sentence = "Today is Wednesday!"

# for char in sentence:  # char is the iterator or loop control variable
#     print(char)




# sentence = "Today is Wednesday!"

# for char in sentence:
#     pass

# print(char)

student_grades = {"Ife": "A", "Sam": "B", "Benjamin": "C", "Praise": "D", "Deborah": "E", "Maryam": "F"}

# for student_grade in student_grades:
#     print(student_grade)
# for student_grade in student_grades.keys():
#     print(student_grade)
# for student_grade in student_grades.values():
#     print(student_grade)

# for student_grade in student_grades.items():
#     print(student_grade)

# for student, grade in student_grades.items():
#     print(student)
#     print(grade)
# for student, grade in student_grades.items():
#     print(student)
#     print(grade)



# states_and_capitals = {"Osun": "Osogbo", "Ekiti": "Ado-Ekiti", "Delta": "Asaba", "Oyo": "Ibadan", "Anambra": "Awka"}

# for state, capital in states_and_capitals.items():
#     print(f"The capital of {state} is {capital}")



# actions = ["sleep", "walk", "skip", "run", "stop", "fall"]

# for action in actions:
#     if action == "skip":
#         continue
#     print(action)


# actions = ["sleep", "walk", "skip", "run", "stop", "fall"]

# for action in actions:
#     if action == "stop":
#         break
#     print(action)


# actions = ["sleep", "walk", "skip", "run", "stop", "fall"]

# for action in actions:
#     print(action)
#     if action == "stop":
        # break


# print(set(range(41)))

# for num in range(20):
#     print(num)



# for num in [1, 8, 3, 78, 287]:
#     print(num)



# for num in range(29, 101, 2):
#     print(num)


# for num in range(10, 1, -2):
#     print(num)


# Count all the even numbers from 23 to 55

# streaming_services = ("Netflix", "Amazon Prime", "Hulu", "Disney Plus", "UEFA TV", "AppleTV")

# for i in range(len(streaming_services)):
#     streaming_service = streaming_services[i]
#     print(streaming_service)



# month_name = "September"

# for i in range(len(month_name)):
#     print(month_name[i])




# streaming_services = ("Netflix", "Amazon Prime", "Hulu", "Disney Plus", "UEFA TV", "AppleTV")
# print(list(enumerate(streaming_services)))


# for index, streaming_service in enumerate(streaming_services):
#     print(f"Streaming service at index {index} is {streaming_service}")


# month_name = "September"
# # print(list(enumerate(month_name)))

# for index, char in enumerate(month_name):
#     print(f"Index {index}: {char}")



# streaming_services = ("Netflix", "Amazon Prime", "Hulu", "Disney Plus", "UEFA TV", "AppleTV")

# for index, service in enumerate(streaming_services):
#     print(f"{index+1}. {service}")
# 1. Netflix
# 2. Amazon Prime
# 3. Hulu
# 4. Disney Plus
# 5. UEFA TV
# 6. AppleTV


# streaming_services = ("Netflix", "Amazon Prime", "Hulu", "Disney Plus", "UEFA TV", "AppleTV")

# for index, service in enumerate(streaming_services, start=1):
#     print(f"{index}. {service}")


# for num in range(29, 101, 2):
# for num in range(101, 29, 2):
#     print(num)
# else:
#     print("Else block running")


# for name in []:
#     print(name)
# else:
#     print("Else block")



# streaming_services = ("Netflix", "Amazon Prime", "Hulu", "Disney Plus", "UEFA TV", "AppleTV")

# for streaming_service in streaming_services:
#     print(streaming_service)
#     for char in streaming_service:
#         print(char)




# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]

# for adjective in adjectives:
#     for animal in animals:
#         print(f"{adjective} {animal}")


# adjectives = ["fierce", "majestic", "playful"]
# animals = ["lion", "eagle", "dolphin"]

# print(list(zip(adjectives, animals)))

# for adjective, animal in zip(adjectives, animals):
#     print(f"{adjective} {animal}")


# adjectives = ["fierce", "majestic", "playful", "hungry", "proud", "angry"]
# animals = ["lion", "eagle", "dolphin"]

# for adjective, animal in zip(adjectives, animals):
#     print(f"{adjective} {animal}")


# adjectives = ["fierce", "majestic", "playful", "hungry", "proud", "angry"]
# animals = ["lion", "eagle", "dolphin"]

# for i in range(len(animals)):
#     adjective = adjectives[i]
#     animal = animals[i]
#     print(f"{adjective} {animal}")



# adjectives = ["fierce", "majestic", "playful", "hungry", "proud", "angry"]
# animals = ["lion", "eagle", "dolphin"]
# lists = [adjectives, animals]
# shortest_list = min(lists, key=len)

# for i in range(len(shortest_list)):
#     adjective = adjectives[i]
#     animal = animals[i]
#     print(f"{adjective} {animal}")




# streaming_services = ("Netflix", "Amazon Prime", "Hulu", "Disney Plus", "UEFA TV", "AppleTV")

# print(min(streaming_services))
# # print(min(streaming_services, key=len))
# print(max(streaming_services, key=len))


# for name in ["James", "John", "Jenny", "Jake"]:
#     pass


# 13. Collect a string from the user and only print put the words that start with the letter 
# ‘S’. Example:
# Input: “Print only the words that start with s in this sentence”
# Output: 
# start
# s
# Sentence
# Input: "I love to code. On Saturday, I will code again. Serena will go with me to school tomorrow."
# Output:
# Saturday
# Serena
# school


# sentence = input("Enter a sentence: ").strip().lower()

# cleaned_chars = []

# for char in sentence:
#     if char.isalpha() or char.isspace():
#         cleaned_chars.append(char)

# print(cleaned_chars)

# sentence = "".join(cleaned_chars)

# # algorithm
# # 1. Break the sentence down into words
# # 2. Go through each word
# # 3. If it starts with s, print it
# # 4. Else, skip it

# words = sentence.split()

# for word in words:
#     if word.startswith("s"):
#         print(word)



# hippoppotamus
# HiPpOpPoTaMuS


# FORGIVEnesS
# FoRgIvEnEsS


# 1. Collect the string from the user
# 2. Create a place to store the final result
# 3. Go through every char in the string
# 4. Capitalize every character at an even index, and lower case every char at an odd index 
# and the new char to the end of the store.

# text = input("Enter some text: ").strip()

# result = []

# for index, char in enumerate(text):
#     if index % 2 == 0:
#         result.append(char.upper())
#     else:
#         result.append(char.lower())

# result = "".join(result)
# print(result)


# text = input("Enter some text: ").strip()

# result = []


# upper = True
# for char in text:
#     if upper:
#         result.append(char.upper())
#     else:
#         result.append(char.lower())
#     upper = not upper

# result = "".join(result)
# print(result)




# --------------------------------LIST COMPREHENSIONS--------------------------------

# verbs = ["dance", "play", "sing", "draw", "laugh", "think", "cry", "smile", "run"]
# # verbs_copy = verbs[::]

# verbs_upper = []

# for verb in verbs:
#     verbs_upper.append(verb.upper())

# print("verbs:", verbs)
# print("verbs_upper:", verbs_upper)


# verbs = ["dance", "play", "sing", "draw", "laugh", "think", "cry", "smile", "run"]
# verbs_upper = [verb.upper() for verb in verbs]


# print("verbs:", verbs)
# print("verbs_upper:", verbs_upper)

# countries = ["Japan", "Nigeria", "Ghana", "Korea", "China", "U.S.A", "Canada", "Germany"]
# developing = ["Nigeria", "Ghana"]
# are_developing = []

# for country in countries:
#     are_developing.append(country in developing)

# print(are_developing)


# countries = ["Japan", "Nigeria", "Ghana", "Korea", "China", "U.S.A", "Canada", "Germany"]
# developing = ["Nigeria", "Ghana"]

# # [False, True, True, False, False, False, False, False]

# are_developing = [country in developing for country in countries]

# print(are_developing)


# ["Japan", "Korea", "China", "U.S.A", "Canada", "Germany"]

# # 1. Transformation / Mapping ✅
# # 2. Conditional Filtering

# countries = ["Japan", "Nigeria", "Ghana", "Korea", "China", "U.S.A", "Canada", "Germany"]
# developing = ["Nigeria", "Ghana"]
# developed = [country for country in countries if country not in developing]
# print(developed)



# words = ["sneak", "socks", "pool", "mute", "laptop", "red", "see"]
# # [True, True, False, False, False, False, True]

# start_with_s = [word.lower().startswith("s") for word in words]

# print(start_with_s)

# # start_with_s_only = [word for word in words if word.lower().startswith("s")]
# dont_start_with_s_only = [word for word in words if not word.lower().startswith("s")]

# # print(start_with_s_only)
# print(dont_start_with_s_only)


# 1. Transformation / Mapping ✅
# 2. Conditional Filtering ✅


# bodies_of_water = ["stream", "ocean", "RIVer", "lagoon", "sea", "lake", "pond"]

# 1. Give me every body of water except "river"

# all_bodies_except_river = [body for body in bodies_of_water if body.lower() != "river"]
# print(all_bodies_except_river)

# 2. [False, True, True, False, True, True, True] -> do the bodies of water have 5 or less chars?

# catholic_saints = ["Benedict", "PAUL", "John", "Peter", "BENJAMIN", "Winifred"]
# # 1. [False, True, False, False, True, False]

# are_upper = [saint.isupper() for saint in catholic_saints]
# print(are_upper)

# # 2. ["PAUL", "BENJAMIN"]
# upper_saints = {saint for saint in catholic_saints if saint.isupper()}
# print(upper_saints)



# catholic_saints = ["Benedict  ", "PAUL", "John", "  Peter", "BENJAMIN ", "Winifred"]
# {"Benedict": 8, "PAUL": 4, "John": 4, "Peter": 5, "BENJAMIN": 8, "Winifred": 8}

# len_catholic_saints = {name: len(name.strip()) for name in catholic_saints}
# print(len_catholic_saints)


# things_that_move_in_the_air = ["birds", "rocket", "aeroplane", "witches", "chopper", "jet", "drone"]
# {"birds": 0, "rocket": 1, "aeroplane": 2, "witches": 1, "chopper": 1, "jet": 1, "drone": 1}

# no_of_e_in_things = {thing: thing.count("e") for thing in things_that_move_in_the_air}

# print(no_of_e_in_things)


# catholic_saints = ["Benedict  ", "PAUL", "John", "  Peter", "BENJAMIN ", "Winifred"]
# are_upper = [saint.isupper() for saint in catholic_saints]
# # Are all the names uppercase?

# are_all_upper = all(are_upper)
# print(are_all_upper)

# # Is there at least one upper case name?
# any_upper = any(are_upper)
# print(any_upper)
# --------------------------------LIST COMPREHENSIONS--------------------------------



# even_nos = [num for num in range(1, 50) if num % 2 == 0]
# print(even_nos)





# --------------------------------GENERATORS--------------------------------
# catholic_saints = ["Benedict  ", "PAUL", "John", "  Peter", "BENJAMIN ", "Winifred"]
# all_upper = all(saint.isupper() for saint in catholic_saints)
# print(all_upper)


# catholic_saints = ["Benedict  ", "PAUL", "John", "  Peter", "BENJAMIN ", "Winifred"]
# any_upper = any(saint.isupper() for saint in catholic_saints)
# print(any_upper)


# 1. Create a list of the square of each number
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]
digits = [1, 2, 3, 4, 5]


# 2. Create a list of names that contain the letter 'a'
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: ["Sara", "Amanda"]
names = ["John", "Sara", "Mike", "Amanda"]


# 3. Create a list of Booleans indicating if each number is greater than 10
# Input: [5, 12, 3, 18, 7]
# Expected Output: [False, True, False, True, False]
values = [5, 12, 3, 18, 7]


# 4. Create a list of the last characters of each word
# Input: ["dog", "cat", "lion", "tiger"]
# Expected Output: ["g", "t", "n", "r"]
animals = ["dog", "cat", "lion", "tiger"]

# 5. Are all the numbers greater than 10?
# Input: [5, 12, 3, 18, 7]
# Expected Output: False
values = [5, 12, 3, 18, 7]


# 6. Is there any name that contains the letter 'a'?
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: True
names = ["John", "Sara", "Mike", "Amanda"]

# 7. Get only the numbers that are divisible by 3 between 12 and 52.

# --------------------------------GENERATORS--------------------------------


# names = ["John", "Sara", "Mike", "Amanda"]
# any_names_with_a = any(name for name in names if "a" in name.lower())
# # print([name for name in names if "a" in name.lower()])
# print(any_names_with_a)
# print(any("a" in name for name in names))


# --------------------------------LIST COMPREHENSION & GENERATORS EXERCISES--------------------------------
# 1. Create a list of the square of each number
# Input: [1, 2, 3, 4, 5]
# Expected Output: [1, 4, 9, 16, 25]
digits = [1, 2, 3, 4, 5]


# 2. Create a list of names that contain the letter 'a'
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: ["Sara", "Amanda"]
names = ["John", "Sara", "Mike", "Amanda"]


# 3. Create a list of Booleans indicating if each number is greater than 10
# Input: [5, 12, 3, 18, 7]
# Expected Output: [False, True, False, True, False]
values = [5, 12, 3, 18, 7]


# 4. Create a list of the last characters of each word
# Input: ["dog", "cat", "lion", "tiger"]
# Expected Output: ["g", "t", "n", "r"]
animals = ["dog", "cat", "lion", "tiger"]

# 5. Are all the numbers greater than 10?
# Input: [5, 12, 3, 18, 7]
# Expected Output: False
values = [5, 12, 3, 18, 7]


# 6. Is there any name that contains the letter 'a'?
# Input: ["John", "Sara", "Mike", "Amanda"]
# Expected Output: True
names = ["John", "Sara", "Mike", "Amanda"]

# 7. Are all the words made up of only uppercase letters?
# Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# Expected Output: False
greetings = ["HELLO", "world", "pyTHon", "ROCKS"]

# 8. Is there any word that starts with 'z'?
# Input: ["apple", "zebra", "mango", "lemon"]
# Expected Output: True
words = ["apple", "zebra", "mango", "lemon"]

# 9. Is there any email address that contains ".org"?
# Input: ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# Expected Output: True
emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]

# 10. Are all numbers odd?
# Input: [1, 3, 5, 7, 9]
# Expected Output: True
values = [1, 3, 5, 7, 9]


# 11. Are all words longer than 2 characters?
# Input: ["hi", "dog", "go", "sun"]
# Expected Output: False
words = ["hi", "dog", "go", "sun"]


# 12. Create a list of triple the value of each number
# Input: [2, 4, 6, 8]
# Expected Output: [6, 12, 18, 24]
nums = [2, 4, 6, 8]


# 13. Are all temperatures above 0°C?
# Input: [12, 7, 3, -1, 5]
# Expected Output: False
temperatures = [12, 7, 3, -1, 5]

# 14. Do all words end with a vowel?
# Input: ["banana", "mango", "kiwi", "grape"]
# Expected Output: True
fruits = ["banana", "mango", "kiwi", "grape"]


# 15. Create a list of words in lowercase
# Input: ["HELLO", "WORLD", "PYTHON"]
# Expected Output: ["hello", "world", "python"]
greetings = ["HELLO", "WORLD", "PYTHON"]


# 16. Is there any number less than 0?
# Input: [5, -2, 3, 0, 8]
# Expected Output: True
numbers = [5, 4, 3, 3, 8]


# 17. Create a list of words that contain the letter 'e'
# Input: ["sky", "tree", "rock", "stone"]
# Expected Output: ["tree", "stone"]
items = ["sky", "tree", "rock", "stone"]


# 18. Are all names starting with uppercase letters?
# Input: ["Alice", "Bob", "charlie", "David"]
# Expected Output: False
names = ["Alice", "Bob", "charlie", "David"]



# 19. Is there any sentence longer than 20 characters?
# Input: ["Short one", "This is a much longer sentence", "Okay"]
# Expected Output: True
sentences = ["Short one", "This is a much longer sentence", "Okay"]

# --------------------------------LIST COMPREHENSION & GENERATORS EXERCISES--------------------------------




# --------------------------------ASSIGNMENT CORRECTION--------------------------------
# 1. Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum. Example:
# Input: 1234
# Output: 10 (1+2+3+4)



# 2. Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# Input: "hello world"
# Output: Vowels: 3, Consonants: 7
# 3. Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# Input: 5
# Output:
# 5 x 1 = 5
# 5 x 2 = 10
# 5 x 3 = 15
# ...
# 5 x 12 = 60
# 4. Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# Example:
# Input: "python"
# Output: "nohtyp"
# 5. Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]

# 1. Ask for the comma-sep numbers
# 2. Separate the numbers, now you have a list of str
# 3. Create a place to store the unique numbers
# 4. Go through the list of nums, if the num is not in the storage for unique nums, add it
# 5. Else, skip it


# numbers = input("Enter numbers separated by commas: ").split(",")
# unique_nums = []

# for num in numbers:
#     num = int(num)
#     if num not in unique_nums:
#         unique_nums.append(num)

# print(unique_nums)

# 6. Write a program that takes an integer input n from the user and prints the first 
# n numbers in the Fibonacci sequence. Example:
# Input: 10
# Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

# 1. Collect n from the user
# 2. Do this n - 2 times:
# 3. Add the last number (i) with the one before it (i - 1)


# n = int(input("Enter the value of n: "))
# fibonacci = [0, 1]

# for i in range(1, n - 1):
#     next_num = fibonacci[i - 1] + fibonacci[i]
#     fibonacci.append(next_num)

# print(fibonacci)

# range(1, 6) -> 1, 2, 3, 4, 5
# range(0, 6) -> 0, 1, 2, 3, 4, 5


# n = 8
# 0, 1
# 0, 1, 0 + 1 -> 0, 1, 1
# 0, 1, 1, 1 + 1 -> 0, 1, 1, 2
# 0, 1, 1, 2, 1 + 2 -> 0, 1, 1, 2, 3
# 0, 1, 1, 2, 3, 3 + 2 -> 0, 1, 1, 2, 3, 5
# 0, 1, 1, 2, 3, 5, 3 + 5 -> 0, 1, 1, 2, 3, 5, 8
# 0, 1, 1, 2, 3, 5, 8, 5 + 8 -> 0, 1, 1, 2, 3, 5, 8, 13


# 7. Collect a list of numbers from the user (entered as comma-separated values) and use a 
# loop to find and print the largest number in the list. Don’t use the built-in max 
# function or anything similar.
# Input: "10, 20, 5, 15"
# Output: 20




# 8. Write a program that takes an integer n from the user and calculates the sum of all 
# even numbers from 1 to n. Print the sum.
# Input: 10
# Output: 30 (2 + 4 + 6 + 8 + 10)


# 9. Collect a string from the user and use a loop to count the frequency of each character 
# in the string. Print each character along with its frequency. Example:
# Input: "hello"
# Output:
# h: 1
# e: 1
# l: 2
# o: 1

# text = input("Enter some text: ").lower().strip()
# occurences = {}

# for char in text:
#     if char in occurences:
#         occurences[char] += 1
#     else:
#         occurences[char] = 1

# print(occurences)

# from collections import defaultdict

# text = input("Enter some text: ").lower().strip()
# occurences = defaultdict(int)
# print(occurences)
# for char in text:
#     occurences[char] += 1
# print(dict(occurences))


# text = input("Enter some text: ").lower().strip()
# occurences = {}
# for char in text:
#      occurences[char] = occurences.get(char, 0) + 1

# print(occurences)

# from collections import Counter
# text = input("Enter some text: ").lower().strip()
# print(dict(Counter(text)))



# text = input("Enter some text: ").lower().strip()
# seen_letters = ""

# for char in text:
#     if char in seen_letters:
#         continue
#     seen_letters += char
#     print(char, ":", text.count(char))


# 10.	Write a program that takes an integer n from the user and calculates the sum of 
# squares of all numbers from 1 to n. Print the sum. Example:
# Input: 3
# Output: 14 (1^2 + 2^2 + 3^2)




# 11. 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
# letter of each word. Print the acronym. Example:
# Input: "Portable Network Graphics"
# Output: "PNG"




# 12. 	Collect a string from the user and use a loop to count the number of words in the string. 
# Print the count. Example:
# Input: "Hello world from Python"
# Output: 4

# words = input("Enter some text: ").split()
# no_of_words = 0
# for word in words:
#     no_of_words += 1

# print(no_of_words)

# 13. 	Collect a string from the user and only print put the words that start with the letter 
# ‘S’. Example:
# Input: “Print only the words that start with s in this sentence”
# Output: 
# start
# s
# Sentence
# 14. Print all the even numbers from 1 to 20 using the range function and a loop.
# 15. Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# by 3.


# 16. Go through the string below and if the length of a word is even, print that word.
# st = ‘Print every word in this sentence that has an even number of letters’
# Output: 
# word
# in
# this
# sentence
# that
# an
# even
# number
# of
# 17. Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# "Fizz" instead of the number, and for multiples of five, print "Buzz". For numbers which 
# are multiples of both three and five, print "FizzBuzz".


# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
        

# 1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz
# 16

# 18. You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# Expected Output:
# Ken got grade A
# Mia got grade E
# Rose got grade F
# Henry got grade C
# Suzan got grade B

# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B', 'E', 'A', 'D']

# lists = [names, grades]

# shorter_list = min(lists, key=len)


# for i in range(len(shorter_list)):
#     name = names[i]
#     grade = grades[i]
#     print(f"{name} got grade {grade}")



# 19. Print only the items at even indexes
# items = ['shoe', 'stick', 'toy', 'fruit']

# Expected Output:
# 0: shoe
# 2: toy

# 20. Given two lists of numbers of the same length, print the indices and values
# of where they differ in a list.
# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# Expected output:
# [
# 'Index 1: 8 != 3',
# 'Index 3: 7 != 9',
# 'Index 5: 4 != 0',
# ]

# list1 = [5, 8, 6, 7, 12, 4]
# list2 = [5, 3, 6, 9, 12, 0]

# result = []

# for i in range(len(list1)):
#     if list1[i] != list2[i]:
#         result.append(f'Index {i}: {list1[i]} != {list2[i]}')

# print(result)


# --------------------------------ASSIGNMENT CORRECTION--------------------------------
