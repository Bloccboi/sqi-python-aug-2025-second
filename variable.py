print("I love pizza!")
print("I love pizza!")
print("I love pizza!")
print("I love pizza!")
print("I love pizza!")
print("I love pizza!")
print("I love pizza!")
print("I love pizza!")

# create two variables,number_of_kids (number) and location(string)
#print their values

number_of_kids= 5
location= "Lagos"
print(number_of_kids)
print(location)


my_number= 45
print(my_number)

sentence= 'This is a string'
print('This is a string')


my_float= 3.14
print(my_float)


am_dark = True
print(am_dark)

my_wife = None
print(my_wife)

PI =22/7
print(PI)


story = "lionel messi is the goat of football.\nhe  once played for barcelona"
print(story)

story = """I am Ayomide
I am a Boy
I  Study Data Analysis at SQI"""
print(story)

story= '''Nigeria is a country with over 200million people
Our Politicians are Corrupt
Nigeria is in Africa
'''
print(story)




#create a variable called greeting and assign the value"I am happy" to it

greeting = "I am happy"
print(greeting[0])
print(greeting[9])
print(greeting[-1])



# story  = "once upon a time, there lived a king"
# print(story[0:16])
# print(story[18:])
# print(story[0:16:2])
# print(story[32:])
# print(story[:9])
# print(story[-12:-5])

# string[start : end : step]


# 8. Create a multi-line string variable using triple quotes.
# 9. Create a string variable word with the value "Python". Print the first and last characters using indexing.
# 10. Attempt to modify the character at index 2 in the string "Python" from question 9. Print the resulting error message.
# 35. Given the string course_name = "Introduction to Python", use slicing to print:
# The word "Introduction".
# The word "Python".
# 36.	Given the string quote = "To be or not to be, that is the question.", use slicing to print:
# The substring "To be or not to be".
# The substring "that is the question".
# 37. Given the string phrase = "A journey of a thousand miles begins with a single step", use 
# slicing to print:
# The last 5 characters.
# All characters except the last 7.
# 38. Given the string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", use slicing to print:
# Every second letter (A, C, E, ...).
# Every third letter starting from the first letter (A, D, G, ...).
# 39. 	Given the string word = "tenet", use slicing to:
# Reverse the string and print the result.
# 40. 	Given the string sentence = "Learning Python is fun and rewarding!", use slicing to print:
# Characters from index 9 to 19. (Python is f)
# Every second character from index 0 to 10. (Lann y)
# Every third character from the beginning to the end. (LrnPh  nnrai!)
# 41. 	Given the string programming_language = "JavaScript", use slicing to:
# Print the first character.
# Print the last character.
# 42.	Given the string data = "DataScience", use slicing to:
# Print the substring "Science".
# 43.	Given the string greeting = "Good Morning!", use slicing to:
# Print every second character.
# 44.	Given the string name = "Alexander", use slicing to:
# Print the first three characters concatenated with the last three characters.






# 8. Create a multi-line string variable using triple quotes.
message = """line one.
line two.
line three."""
print(message)

# 9. Create a string variable word with the value "Python". Print the first and last characters using indexing.
word = "Python"
print(word[0])
print(word[-1])

# 10. Attempt to modify the character at index 2 in the string "Python" from question 9. Print the resulting error message.
word = "Python"
# word[2] = "X"


# 35. Given the string course_name = "Introduction to Python", use slicing to print:
# The word "Introduction".
# The word "Python".

course_name = "Introduction to Python"
print(course_name[0:13])
print(course_name[17:])


# 36. Given the string quote = "To be or not to be, that is the question.", use slicing to print:
# The substring "To be or not to be".

quote = 'To be or not to be'
print(quote[:18])


# 37. Given the string phrase = "A journey of a thousand miles begins with a single step", use 
# slicing to print:
# The last 5 characters.
# All characters except the last 7.

phrase = "A journey of a thousand miles begins with a single step"

print(phrase[-5:])  
print(phrase[:-7])


# 38. Given the string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", use slicing to print:
#  Every second letter (A, C, E, ...).
# Every third letter starting from the first letter (A, D, G, ...).

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabet[::2])
print(alphabet[::3])

# 39. Given the string word = "tenet", use slicing to:
#  Reverse the string and print the result.

word = "tenet"
print(word[::-1])


# 40. 	Given the string sentence = "Learning Python is fun and rewarding!", use slicing to print:
# Characters from index 9 to 19. (Python is f)
# Every second character from index 0 to 10. (Lann y)
# Every third character from the beginning to the end. (LrnPh  nnrai!)

sentence = "Learning Python is fun and rewarding!"
print(sentence[9:20])  
print(sentence[0:11:2]) 
print(sentence[::3])  


# 41. 	Given the string programming_language = "JavaScript", use slicing to:
# Print the first character.
# Print the last character.

programming_language = "JavaScript"
print(programming_language[0])
print(programming_language[-1])


#  42.Given the string data = "DataScience", use slicing to:
#  Print the substring "Science".

course_name = "DataScience"
print(course_name[4:])


# Given the string greeting = "Good Morning!", use slicing to:
#  Print every second character.

greeting = "Good Morning!"
print(greeting[::2])

#  Given the string name = "Alexander", use slicing to:
#  Print the first three characters concatenated with the last three characters.

name = "Alexander"
name[:3]
name[-3:] 
print(name[:3] + name[-3:])


location = "SQI"
greeting = "Good morning,"
sentence = location + " " + greeting
print(sentence)

favorite_food = "yam and egg"
favorite_num = 34
slept_early = False
distance = 34.7


sentence = "It is " + str(slept_early)+ " that I Slept early last night.\nMy favorite food is "+  favorite_food + ".\nThe distance from my school to house is"+" "+ str(distance) + "km"

print(sentence)

sentence = """It is {} that I slept early last night.my favorite food is {}. 
the distance from my school to my house is {}km.
My favorite number is {}.""".format(slept_early,favorite_food,distance,favorite_num)
print(sentence)
 
sentence = f"""It is{slept_early} that I slept early last night.My favorite food is {favorite_food}.The distance from my school to house is {distance}km.
my favorite number is{favorite_num}"""
print(sentence)

age = 12
sentence = "I am 12 years old."
print("I am "+ str(age) + " years old")
print("I am {} years  old".format(age))
print(f"I am {age} years old")


# 1. Create two string variables: first_name with value "John" and last_name with value 
# "Smith". Concatenate them together with a space in between and print the result.
# 2. Given the string word = "Python", print the first character.
# 3.Create a string variable greeting with the value "Hello". Use string interpolation to insert the name "Alice" into the greeting and print the result.
# 4.Given the strings part1 = "Data" and part2 = "Science", concatenate them to form "DataScience" and print the result.
# 5.Given the string phrase = "Welcome", print the last character using negative indexing.
# 6.Create a string variable food with the value "pizza". Use string interpolation to create the sentence "I love pizza" and print it.
# 7.Given the strings str_1 = "Good" and str_2 = "Morning", concatenate them with a space in between to form "Good Morning" and print the result.
# 8.Given the string text = "Concatenate", print the character at index 5.
# 9.Create a variable age with the value 25. Use string interpolation to create the sentence "I am 25 years old" and print it.
# 10.Create three string variables: city = "New", space = " ", and country = "York". Concatenate them to form "New York" and print the result.
# 11.Given the string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", print the 10th character.
# 12.Create variables day = "Sunday" and activity = "hiking". Use string interpolation to create the sentence "On Sunday, I am going hiking" and print it.
# 13.Given the strings a = "Super" and b = "Hero", concatenate them to form "SuperHero" and print the result.
# 14.Given the string universe = "MilkyWay", print the third character from the end using 
# negative indexing.
# 15. 	Create variables item = "book" and price = 12.99. Use string interpolation to create the 
# sentence "The price of the book is $12.99" and print it.
# 16. 	Given the strings hello = "Hello" and world = "World", concatenate them with a comma and space 
# in between to form "Hello, World" and print the result.
# 17. 	Given the string sequence = "ABCDEFG", print the character at index 4.
# 18. 	Create a variable language = "Python". Use string interpolation to create the sentence "I am 
# learning Python" and print it.
# 19. 	Given the strings start = "Once upon a" and end = " time", concatenate them to form "Once upon a 
# time" and print the result.
# 20. 	Given the string sports = "Basketball", print the second character.


# 1.  Create two string variables: first_name with value "John" and last_name with value 
#  "Smith". Concatenate them together with a space in between and print the result.
first_name = "John"
last_name = "Smith"
print(first_name + ' ' +last_name)

# 2. Given the string word = "Python", print the first character.
word = "Python"
print(word[0])

# 3.Create a string variable greeting with the value "Hello". Use string interpolation to insert the name "Alice" into the greeting and print the result.
greeting = "Hello"
name = "Alice"
print(f"{greeting}, {name}")

# 4.Given the strings part1 = "Data" and part2 = "Science", concatenate them to form "DataScience" and print the result.
part1 ="Data"
part2 ="Science"
print(part1+part2)

# 5.Given the string phrase = "Welcome", print the last character using negative indexing.
phrase = "Welcome"
print(phrase[-1])

# 6.Create a string variable food with the value "pizza". Use string interpolation to create the sentence "I love pizza" and print it.
food ="pizza"
print(f"I love {food}")

# 7.Given the strings str_1 = "Good" and str_2 = "Morning", concatenate them with a space in between to form "Good Morning" and print the result.
str_1 = "Good"
str_2 = "Morning"
print(str_1+ ' '+str_2)

# 8.Given the string text = "Concatenate", print the character at index 5.
text = "Concatenate"
print(text[5])

# 9.Create a variable age with the value 25. Use string interpolation to create the sentence "I am 25 years old" and print it.
age = 25
print(f"I am {age} years old")

# 10.Create three string variables: city = "New", space = " ", and country = "York". Concatenate them to form "New York" and print the result.
city = "New"
space = " "
country = "York"
print(city+space+country)

# 11.Given the string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", print the 10th character.
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
print(alphabet[9])

# 12.Create variables day = "Sunday" and activity = "hiking". Use string interpolation to create the sentence "On Sunday, I am going hiking" and print it.
Day = "Sunday"
activity ="hiking"
print(f"On {Day},I am going {activity}")

# 13.Given the strings a = "Super" and b = "Hero", concatenate them to form "SuperHero" and print the result.
a = "Super"
b = "Hero"
print(a+b)

# 14.Given the string universe = "MilkyWay", print the third character from the end using 
# negative indexing.
universe = "MilkyWay"
print()

# 15. Create variables item = "book" and price = 12.99. Use string interpolation to create the 
# sentence "The price of the book is $12.99" and print it.
item = "book"
price = 12.99
print(f"The price of the book is {price}")

# 16. 	Given the strings hello = "Hello" and world = "World", concatenate them with a comma and space 
# in between to form "Hello, World" and print the result.
hello = "Hello"
world = "World"
# print(hello+","+" "+world)
print(hello+ ", " + world)

# 17. Given the string sequence = "ABCDEFG", print the character at index 4.
alphabets = "ABCDEFG"
print(alphabets[4])

# 18. 	Create a variable language = "Python". Use string interpolation to create the sentence "I am 
# learning Python" and print it.
language = "Python"
print(f"I am learning {language}")

# 19. 	Given the strings start = "Once upon a" and end = " time", concatenate them to form "Once upon a 
# time" and print the result.
start = "Once upon a"
end = "time"
print(start + " "+end)

# 20. 	Given the string sports = "Basketball", print the second character.
sports = "Basketball"
print(sports[1])

# 2. Create a variable named x and assign the value 50 to it.
# 6.Create two string variables: first_name with value "John" and last_name with value "Doe". Concatenate them together and print the result.
# 7.Create a string variable message with the value "Hello, ". Interpolate the variable name (assigned the value "Alice") into the message and print the result.

# 2. Create a variable named x and assign the value 50 to it.
x = 50

# 6.Create two string variables: first_name with value "John" and last_name with value "Doe". Concatenate them together and print the result.
first_name = "John"
last_name ="Doe"
print(first_name+' '+last_name)

# 7.Create a string variable message with the value "Hello, ". Interpolate the variable name (assigned the value "Alice") into the message and print the result.
message = "Hello,"
value = "Alice"
print(f"{message}{value}")


# 17.	Convert a string “James John Kennedy” called “names” to a list using the string 
# .split() method. Store the result in a list called “names_list”
# 18.	You have a list of cities called cities_list containing ['New York', 'Los Angeles', 
# 'Chicago']. Convert this list into a single string where each city is separated by a 
# semicolon and a space. Store the result in a string called cities_string.
# 9.	Create a string variable sentence with the value "the quick brown fox jumps over the 
# lazy dog". Capitalize the first letter of the string and 
# print the result.
# 20. 	Create a string variable book_title with the value "to kill a mockingbird". Capitalize 
# the first letter of each word and print the result.
# 21. 	Create a string variable text with the value "hello world". Count the number of 
# occurrences of the letter 'o' and print the result.
# 22. 	Create a string variable filename with the value "document.txt". Check if the string 
# starts with "doc" and print the result.
# 23.	Create a string variable url with the value "https://www.example.com". Check if the 
# string ends with ".com" and print the result.
# 24.	Create a string variable phrase with the value "find the needle in the haystack". Find 
# the position of the word "needle" and print the result.
# 25.	Create a string variable template with the value "Hello, {}. Welcome to {}.". Use the 
# format() method to replace the placeholders with "Alice" and "Wonderland" and print the 
# Result. Bonus point if you can do it with the f-string and concatenation methods also.
# 26.	Create a string variable `quote` with the value "To be or not to be". Find the position 
# of the word "not" and print the result.
# 27.	Create a string variable word with the value "hello". Check if all characters in the 
# string are lowercase and print the result.
# 28.	Create a string variable shout with the value "HELLO". Check if all characters in the 
# string are uppercase and print the result.
# 29.	Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# lowercase and print the result.
# 30. 	Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# uppercase and print the result.
# 31. 	Create a string variable padded_text with the value " hello ". Remove leading whitespace and 
# print the result.
# 32. 	Create a string variable padded_text with the value " hello ". Remove trailing whitespace and 
# print the result.
# 33.	Create a string variable padded_text with the value " hello ". Remove both leading and trailing 
# whitespace and print the result.
# 34.	Create a string variable greeting with the value "Hello, World!". Replace "World" with "Alice" 
# and print the result.


# 17.Convert a string “James John Kennedy” called “names” to a list using the string 
names = "James John Kennedy"
names_list = names.split()
print(names_list)

# 18.You have a list of cities called cities_list containing ['New York', 'Los Angeles', 
# 'Chicago']. Convert this list into a single string where each city is separated by a 
# semicolon and a space. Store the result in a string called cities_string.

cities_list = ['New York', 'Los Angeles', 'Chicago']
cities_string = '; '.join(cities_list)
print(cities_string)

# 19.Create a string variable sentence with the value "the quick brown fox jumps over the lazy dog". Capitalize the first letter of the string and print the result.
sentence = "the quick brown fox jumps over the  lazy dog"
sentence = sentence.capitalize()
print(sentence)

# 20. Create a string variable book_title with the value "to kill a mockingbird". Capitalize the first letter of each word and print the result.
book_title = "to kill a mockingbird"
book_title = book_title.title()
print(book_title)

# 21. Create a string variable text with the value "hello world". Count the number of  occurrences of the letter 'o' and print the result.
text = "hello world"
print(text.count('o'))

# 22. Create a string variable filename with the value "document.txt". Check if the string starts with "doc" and print the result.
filename = "document.txt"
result =filename.startswith("doc")
print(result)

# 23. Create a string variable url with the value "https://www.example.com". Check if the string ends with ".com" and print the result.
url = "https://www.example.com"
website =url.endswith(".com")
print(website)

# 24. Create a string variable phrase with the value "find the needle in the haystack". Find the position of the word "needle" and print the result.
value ="find the needle in the haystack"
print(value.find('needle'))

# 25. Create a string variable template with the value "Hello, {}. Welcome to {}.". Use the 
# format() method to replace the placeholders with "Alice" and "Wonderland" and print the 
# Result. Bonus point if you can do it with the f-string and concatenation methods also.
template = "Hello, {}.Welcome to {}"

# USING FORMAT METHOD
template = "Hello, {}. Welcome to {}."
result_format = template.format("Alice", "Wonderland")
print(result_format)

# Using f-string method
name ="Alice"
place ="Wonderland"
result_fstring =f"Hello,{name}. Welcome to {place}"
print(result_fstring)

# Using string concatenation method
name = "Alice"
place = "Wonderland"
result_concat = "Hello, " + name + ". Welcome to " + place + "."
print(result_concat)

# 26. Create a string variable `quote` with the value "To be or not to be". Find the position of the word "not" and print the result.
quote = "To be or not to be"
print(quote.find("not"))

# 27. Create a string variable word with the value "hello". Check if all characters in the string are lowercase and print the result.
word ="hello"
print(word.islower())

# 28. Create a string variable shout with the value "HELLO". Check if all characters in the  string are uppercase and print the result.
value = "HELLO"
print(value.isupper())

# 29. Create a string variable mixed_case with the value "PyThOn". Convert all characters to lowercase and print the result.
mixed_case = "PyThOn"
lower_case = mixed_case.lower()
print(lower_case)

# 30. Create a string variable mixed_case with the value "PyThOn". Convert all characters to  uppercase and print the result.
mixed_case ="PyThon"
upper_case = mixed_case.upper()
print(upper_case)

# 31. Create a string variable padded_text with the value " hello ". Remove leading whitespace and print the result.
padded_text = " hello "
trimmed_text = padded_text.lstrip()
print(trimmed_text)

#  32. Create a string variable padded_text with the value " hello ". Remove trailing whitespace and  print the result
padded_text = " hello "
trimmed_text = padded_text.rstrip()
print(trimmed_text)

# 33. Create a string variable padded_text with the value " hello ". Remove both leading and trailing whitespace and print the result.
padded_text = " hello "
trimmed_text = padded_text.strip()
print(trimmed_text)

# 34.	Create a string variable greeting with the value "Hello, World!". Replace "World" with "Alice" and print the result.
greeting = "Hello, World!"
new_greeting =greeting.replace("World","Alice")
print(new_greeting)


 
means_of_transport = ["plane","ship","train","broom","car"]
print(means_of_transport[0])
print(means_of_transport[4])
print(means_of_transport[-1])
means_of_transport.insert(5,"feet")
means_of_transport.insert(2,"canoe")
means_of_transport.remove("broom")
print("car" in means_of_transport)
means_of_transport[4] = "horse"
print(means_of_transport)


