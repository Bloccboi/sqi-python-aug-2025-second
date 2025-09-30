# # print("Hello World!!")


# # 11. Assign values "Orange", "Banana", "Cherry" to multiple variables x, y and z in one line respectively.
# # 12. Assign the values 10, "John", and True to the variables age, name, and is_student in a 
# # single line.
# # 13. Swap the values of x and y, where x = 5 and y = 10, without using a temporary variable.
# # 14.Create a list of numbers with values 1, 2, and 3. Unpack the list into separate 
# # variables a, b, and c.
# # 15.Convert a string variable called height from “1.35” to a float.
# # 16.Predict the output of the following statements:
# # a) bool("")
# # b) bool(123)
# # c) bool(["apple", "cherry", "banana"])
# # d) bool(False)
# # e) bool(None)
# # f) bool(0)
# # g) bool("abc")
# # h) bool(())
# # i) bool([])


# # # # 11. Assign values "Orange", "Banana", "Cherry" to multiple variables x, y and z in one line respectively.
# # x,y,z = "Orange","Banana","Cherry"

# # # # 12. Assign the values 10, "John", and True to the variables age, name, and is_student in a 
# # # # single line.
# # age, name, is_student = 10, "John", True
# # print(age)
# # print(name)
# # print(is_student)
# # print("age =", age, ", name =", name, ", is_student =", is_student)

# # # # 13. Swap the values of x and y, where x = 5 and y = 10, without using a temporary variable.
# # x,y = 5,10
# # x,y = y,x
# # print(x,y)
# # print(" x =", x, ", y =", y)

# # # # 14.Create a list of numbers with values 1, 2, and 3. Unpack the list into separate  variables a, b, and c.
# # numbers = [1,2,3]
# # a,b,c = numbers
# # print("a=",a,",b=",b,"c=",c)

# # # # 15.Convert a string variable called height from “1.35” to a float.
# # height = 1.35
# # height =float(height)
# # print("height=",height,"type:",type(height))

# # # # 16.Predict the output of the following statements:
# # # a) bool("")--> false(Empty string is false)
# # # b) bool(123)--> True
# # # c) bool(["apple", "cherry", "banana"])--> True(Non empty list is true)
# # # d) bool(False)--> False
# # # e) bool(None)-->False
# # # f) bool(0)-->False(zero is false)
# # # g) bool("abc")-->True(Non-empty string is true)
# # # h) bool(())-->false(Empty tuple is false)
# # # i) bool([])-->false(Empty list is false)



# # # # Sample Execution:
# # # # Enter your name: David
# # # # Enter the activity you did (e.g., running, cycling): Hiking
# # # # Enter the duration of the activity (in minutes): 120
# # # # Enter the calories burned: 850
# # # #
# # # # Fitness Activity:
# # # # Name: David
# # # # Activity: Hiking
# # # # Duration: 120 minutes
# # # # Calories Burned: 850 kcal
# # # #
# # # # Task:
# # # # Write a Python program that works exactly like the sample above.
# # # # The program should ask the user for their name, activity, duration, and calories burned,
# # # # and then print the details in the same format.

# # # # Solution
# # name = input("Enter your name: ")
# # activity = input("Enter the activity you did (e.g., running, cycling): ")
# # duration = input("Enter the duration of the activity (in minutes): ")
# # calories = input("Enter the calories burned: ")

# # print("\nFitness Activity:")
# # print(f"Name: {name}")
# # print(f"Activity: {activity}")
# # print(f"Duration: {duration} minutes")
# # print(f"Calories Burned: {calories} kcal")


# # # # NOW DO THESE:
# # # # Exercise 1:
# # # # Sample Execution:
# # # # Enter your first name: Alice
# # # # Enter your last name: Johnson
# # # #
# # # # Full Name: Alice Johnson
# # # #
# # # # Task:
# # # # Write a Python program that asks the user for their first name and last name,
# # # # # then prints their full name in the format shown above.
# # # solution
# # first_name = input("Enter your first name: ")
# # last_name = input("Enter your last name: ")
# # print("Full Name:",first_name,last_name)


# # # # Exercise 2:
# # # # Sample Execution:
# # # # Enter the length of the rectangle: 8
# # # # Enter the width of the rectangle: 5
# # # #
# # # # Area of the rectangle: 40
# # # #
# # # # Task:
# # # # Write a Python program that calculates the area of a rectangle.
# # # # The program should ask for length and width, then display the area.
# # # solution

# # length = float(input("Enter the length of the triangle:"))
# # width = float(input("Enter the width of the triangle:"))
# # area = length * width
# # print("Area of rectangle:",int(area))

# # # # Exercise 3:
# # # # Sample Execution:
# # # # Enter the temperature in Celsius: 25
# # # #
# # # # Temperature in Fahrenheit: 77.0
# # # #
# # # # Task:
# # # # Create a Python program that converts a temperature from Celsius to Fahrenheit.
# # # # Formula: F = (C × 9/5) + 32

# # celcius = float(input("Enter the temperature in celcius: "))
# # fahrenheit = (celcius * 9/5) + 32
# # print("Temperature in Fahrenheit:",fahrenheit)


# # # # Exercise 4:
# # # # Sample Execution:
# # # # Enter the number of apples: 4
# # # # Enter the number of bananas: 6
# # # #
# # # # Total fruits: 10
# # # #
# # # # Task:
# # # # Write a program that asks the user for the number of apples and bananas,
# # # # then prints the total number of fruits.
# # # solution
# # number_of_apples = int(input("Enter the number of apples: "))
# # number_of_bananas =int(input("Enter the number of bananas: "))
# # Total_fruits = number_of_apples + number_of_bananas
# # print("Total_fruits:",Total_fruits)

# # # # Exercise 5:
# # # # Sample Execution:
# # # # Enter your age: 30
# # # #
# # # # You will be 35 years old in 5 years.
# # # #
# # # # Task:
# # # # Create a program that asks the user for their age,
# # # # then calculates and prints how old they will be in 5 years.

# # # #Solution
# # age = int(input("Enter your age:"))
# # future_age = age + 5
# # print(f"You will be {future_age} years old in 5 years.")

# # # # Exercise 6:
# # # # Sample Execution:
# # # # Enter the distance in kilometers: 10
# # # #
# # # # Distance in miles: 6.21371
# # # #
# # # # Task:
# # # # Write a Python program that converts kilometers to miles.
# # # # 1 kilometer = 0.621371 miles.

# # # #Solution
# # kilometers = float(input("Enter the distance in kilometers: "))
# # miles =  kilometers * 0.621371
# # print("Distance in miles:",miles)

# # # # Exercise 7:
# # # # Sample Execution:
# # # # Enter your favorite color: Blue
# # # # Enter your favorite food: Pizza
# # # #
# # # # Your favorite color is Blue and your favorite food is Pizza.
# # # #
# # # # Task:
# # # # Write a Python program that asks the user for their favorite color and food,
# # # # then displays the message exactly like the example.

# # # #Solution
# # color = input("Enter your favorite color: ")
# # food = input("Enter your favorite color: ")
# # print(f"Your favorite color is {color} and your favorite food is {food}.")

# # # # # Exercise 8:
# # # # Sample Execution:
# # # # Enter the price of an item: 50
# # # # Enter the discount percentage: 20
# # # #
# # # # Price after discount: 40.0
# # # #
# # # # Task:
# # # # Write a program that calculates the final price after a discount.
# # # # Formula: final_price = price - (price × discount/100)

# # # Solution
# # price_of_item = float(input("Enter the price of an item: "))
# # discount_percentage = float(input("Enter the discount percentage: "))
# # final_price = price_of_item - (price_of_item * discount_percentage / 100)
# # print("Price after discount: ",final_price)


# # # # Exercise 9:
# # # # Sample Execution:
# # # # Enter the number of hours worked: 40
# # # # Enter your hourly rate: 15
# # # #
# # # # Weekly pay: 600
# # # #
# # # # Task:
# # # # Write a program that calculates a worker's weekly pay
# # # # based on hours worked and hourly rate.

# # # solution
# # number_of_hours = float(input("Enter the number of hours worked: "))
# # hourly_rate = float(input("Enter your hourly rate: "))
# # Weekly_pay = number_of_hours * hourly_rate
# # print("Weekly pay:",int(Weekly_pay))


# # # # Exercise 10:
# # # # Sample Execution:
# # # # Enter your favorite movie: Inception
# # # # Enter your favorite song: Bohemian Rhapsody
# # # #
# # # # Your favorite movie is Inception and your favorite song is Bohemian Rhapsody.
# # # #
# # # # Task:
# # # # Create a Python program that asks the user for their favorite movie and song,
# # # # then prints them in the same format as the example.

# # # solution
# # # movie =input("Enter your favorite movie: ")
# # # song = input("Enter your favorite song: ")
# # # print (f"Your favorite movie is {movie} and your favorite song is {song}.")


# #1. Write a program that asks the user for their name and then greets them with their 
# # name: Print a greeting message that includes the user's name in the format "Hello, {name}!".
# #2. Ask the user for their birth year and calculate their age. Print the user's age in the 
# # format “You are {age} years old.”.
# #3. Ask the user for their favourite color. Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”.
# #4.Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# # Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.
# #5.Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# # Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# #.Bonus point if you can hide the password input from displaying on the screen as clear text.
# #6.Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.


# #1. Write a program that asks the user for their name and then greets them with their 
# # name: Print a greeting message that includes the user's name in the format "Hello, {name}!".
# # name =input("Enter your name: ")
# # print(f"Hello, {name}!")

# #2. Ask the user for their birth year and calculate their age. Print the user's age in the 
# # format “You are {age} years old.”.
# # age = 26
# # print(f"You are {age} years old.")

# #3. Ask the user for their favourite color. Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”.
# # favorite_color = "Black"
# # print(f"Your favorite color is {favorite_color}.")

# #4. Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.
# # Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.
# # text = input("Enter some text here: ")
# # new_text = text.replace(" ", "").lower()
# # is_palindrome = new_text == new_text [::-1]
# # print(f"It is {is_palindrome} that {text} is a palindrome.")

# #5.Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).
# # Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.
# # Bonus point if you can hide the password input from displaying on the screen as clear text.
# # import getpass
# # pass_word = getpass.getpass("Enter your password: ")
# # is_valid = 8 <= len(pass_word) <= 30
# # print(f"It is {is_valid} that the password fulfils the criteria.")

# # Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.
# # weight = input((f"Enter your weight in kilograms: "))
# # height = input(f"Enter your height in meters: ")
# # bmi = weight / (height ** 2)
# # bmi_rounded =round(bmi,2)
# # print(float)(f"\nYour BMI is {bmi_rounded}")



# # 1.Create a list called fruits with items "apple", "banana", and "orange". Print the first item.
# # 2.Create a list called colors with items "red", "green", "blue". Print the last item using negative indexing.
# # 3.Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7.
# # 4.Create a list called alphabets with items "a", "b", "c", ..., "z". Print a slice from index -3 to the end.
# # 5.Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.
# # 6.Create a list called grades with items "A", "B", "C", "D". Change the values of items from index 1 to index 3 to "X".
# # Create a list called cities with items "New York", "London", "Paris". Insert "Tokyo" at the beginning of the list.
# # Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the list.
# # Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list.
# # Create a list called mixed with items 10, "apple", True. Print the list.
# # Create a tuple called tuple_data with items "a", "b", "c". Convert the tuple into a list.
# # Create a list called books with items "Python", "Java". Append "JavaScript" to the end of the list.
# # Create a list called names with items "Alice", "Bob", "Eve". Insert "Charlie" at index 1.
# # Create two lists called list1 and list2 with items 1, 2, 3 and 4, 5, 6 respectively. Extend list1 with list2.
# # Create a list called students with items "Alice", "Bob". Add items from a tuple ("Charlie", "David") to students.
# # Create a list called colors with items "red", "green", "blue". Remove "green" from the list.
# # Create a list called numbers with items 10, 20, 30, 40. Use the del keyword to remove the item at index 2.
# # 18.	Create a list called fruits with items "apple", "banana", "cherry". Clear the list.
# #  19.	Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically.
# #  20. 	Create a list called ages with items 25, 35, 20. Sort the list in descending order.
# #  21. 	Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
# # "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.
# #  22. 	Create a list called numbers with items 1, 2, 3, 4. Print the list in reverse order.
# #  23.	Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using
# # 	slicing.
# #  24.	Create a list called original with items "one", "two", "three". Create a copy of the list.
# #  25.	Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and 
# # 	list2 together.
# #  26.	Access and print the second subject of the first person in the list.
# # 	data = [
# #     ["Alice", 25, ["Math", "Physics"]],
# #     ["Bob", 30, ["Chemistry", "Biology"]],
# #     ["Charlie", 35, ["History", "Geography"]]
# # ]
# #  27.	Access and print the first value in the list of numbers associated with "San Francisco".
# # 	records = [
# #     ["New York", [10, 20, 30]],
# #     ["San Francisco", [40, 50, 60]],
# #     ["Austin", [70, 80, 90]]
# # ]
# # 28.	Get the first e in Ayo’s gender and Get Ben’s age.
# #  	group = [
# #     ["Ayo", ["Female", 12]],
# #     ["Ben", ["Male", 9]]
# # ]
# #  29.	Get the l in Nina’s gender and Get Tobi’s age
# # 	records = [
# #     ["Tobi", ["Male", [6]]],
# #     ["Nina", ["Female", [7]]]
# # ]
# #  30.	Get the two oo’s in X1’s 2nd mobility status (loose) together (slicing) and Get the battery percentage of R2
# # robot_grid = [
# #     ["R2", ["battery", [98]]],
# #     ["R5", ["status", "active"]],
# #     ["X1", [["joint", "loose"], "error"]]
# # ]
# #  31.	Get the Five in the Jazz song title and Get the duration of the Jazz song
# # playlist = [
# #     ["Jazz", ["Take Five", 5.24]],
# #     ["Pop", ["Blinding Lights", 3.20]],
# #     ["Rock", ["Bohemian Rhapsody", 5.55]]
# # ]
# #  32.	Get the letter v in Tiger’s category and Get the first letter of the Frog’s type
# # animals = [
# #     ["Elephant", ["Herbivore"]],
# #     ["Tiger", ["Carnivore"]],
# #     ["Frog", ["Amphibian"]]
# # ]


# # 1.Create a list called fruits with items "apple", "banana", and "orange". Print the first item.
# fruits =["apple","banana","orange"]
# print(fruits[0])    

# # 2.Create a list called colors with items "red", "green", "blue". Print the last item using negative indexing.
# colors =["red","green","blue"]
# print(colors[-1])

# # 4.Create a list called alphabets with items "a", "b", "c", ..., "z". Print a slice from index -3 to the end.
# alphabets =["a","b","c","d","e","f","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
# print(alphabets[-3:])

# # 5.Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.
# ages =[20,30,40]
# ages[1] = 35
# print(ages)

# # 6.Create a list called grades with items "A", "B", "C", "D". Change the values of items from index 1 to index 3 to "X".
# grades =["A","B","C","D"]
# grades[1:4] = ["X","X","X",]
# print(grades)

# # 7.create a list called cities with items "New York", "London", "Paris". Insert "Tokyo" at the beginning of the list.
# cities = ["New York","London","Paris"]
# cities.insert(0, "Tokyo")
# print(cities)

# #8. Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the list.
# fruits = ["apple","banana","cherry"]
# print(len(fruits))

# #9. Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list.
# prices = [10.5, 20.5, 15.75]
# print(type(prices))

# #10. Create a list called mixed with items 10, "apple", True. Print the list.
# mixed = [10, "apple", True]
# print(mixed)

# # 11.Create a tuple called tuple_data with items "a", "b", "c". Convert the tuple into a list.
# tuple_data = ["a", "b", "c"]
# tuple_data = list(tuple_data)
# print(tuple_data)

# #12. Create a list called books with items "Python", "Java". Append "JavaScript" to the end of the list.
# books = ["Python","Java"]
# books.append("Javascript")
# print(books)

# #13. Create a list called names with items "Alice", "Bob", "Eve". Insert "Charlie" at index 1.
# names =["Alice","Bob","Eve"]
# names.insert(1,"Charlie")
# print(names)

# # 14.Create two lists called list1 and list2 with items 1, 2, 3 and 4, 5, 6 respectively. Extend list1 with list2.
# list_1 = [1,2,3]
# list_2 = [4,5,6]
# list_1.extend(list_2)
# print(list_1)
# # 15. Create a list called numbers with items 10, 20, 30, 40. Use the del keyword to remove the item at index 2.
# numbers = [10,20,30,40]
# del numbers[2]
# print(numbers)

# # 16. Create a list called colors with items "red", "green", "blue". Remove "green" from the list.
# colors = ["red","green","blue"]
# colors.remove("green")
# print(colors)

# # 18. Create a list called fruits with items "apple", "banana", "cherry". Clear the list.
# fruits = ["apple","banana","cherry"]
# fruits.clear()
# print(fruits)

# #  19. Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically.
# items = ["Zoe","Alice","Bob"]
# items.sort()
# print(items)

# # 20. Create a list called ages with items 25, 35, 20. Sort the list in descending order.
# items = [25,35,20]
# items.sort()
# print(items)

# # 21. Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
# # "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.
# list = ["Apple","banana","Orange"]
# list.sort(key= str.lower)
# print(list)

# # 22. Create a list called numbers with items 1, 2, 3, 4. Print the list in reverse order.
# numbers = [1,2,3,4]
# numbers.reverse()
# print(numbers)

# # 23. Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using slicing.
# letters = ["a","b","c","d"]
# letters.reverse()
# letters = letters[::-1]
# print(letters[::-1])

# # 24.Create a list called original with items "one", "two", "three". Create a copy of the list.
# original = ["one","two","three"]
# copy_list = original.copy()
# print("original list:",original)
# print("Copied list:",copy_list)

# # 25.Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and list2 together.
# list_1 = ["a","b",]
# list_2 = ["c","d",]
# joined_list = list_1 + list_2
# print("Joined list:",joined_list)

# # 26.	Access and print the second subject of the first person in the list.
# # # 	data = [
# # #     ["Alice", 25, ["Math", "Physics"]],
# # #     ["Bob", 30, ["Chemistry", "Biology"]],
# # #     ["Charlie", 35, ["History", "Geography"]]
# # # ]
# data = [
#     ["Alice", 25, ["Math", "Physics"]],
#     ["Bob", 30, ["Chemistry", "Biology"]],
#     ["Charlie", 35, ["History", "Geography"]]
# ]
# second_subject = data[0][2][1]
# print("Second Subject:",second_subject)

# # 27.	Access and print the first value in the list of numbers associated with "San Francisco".
# # # 	records = [
# #     ["New York", [10, 20, 30]],
# #     ["San Francisco", [40, 50, 60]],
# #     ["Austin", [70, 80, 90]]

# records = [
#     ["New York", [10, 20, 30]],
#     ["San Francisco", [40, 50, 60]],
#     ["Austin", [70, 80, 90]]
# ]
# first_value = records[1][1][0]
# print("First value for San Fransico",first_value)

# # 28.	Get the first e in Ayo’s gender and Get Ben’s age.
# #  	group = [
# #     ["Ayo", ["Female", 12]],
# #     ["Ben", ["Male", 9]]

# group = [
#     ["Ayo", ["Female", 12]],
#     ["Ben", ["Male", 9]]
# ]
# ayos_gender = group[0][1][0]
# first_e = ayos_gender[ayos_gender.index("e")]
# bens_age = group[1][1][1]        
# print("First 'e' in Ayo's gender:", first_e)
# print("Ben's age:", bens_age)

# # 29.	Get the l in Nina’s gender and Get Tobi’s age
# # 	records = [
# #     ["Tobi", ["Male", [6]]],
# #     ["Nina", ["Female", [7]]]
# # ]

# records = [
#    ["Tobi", ["Male", [6]]],
#     ["Nina", ["Female", [7]]]
# ]
# tobi_gender = records[0][1][0] 
# tobi_number = records[0][1][1][0]
# nina_gender = records[1][1][0]   
# nina_number = records[1][1][1][0] 


# print("Tobi's gender:", tobi_gender)
# print("Tobi's number:", tobi_number)
# print("Nina's gender:", nina_gender)
# print("Nina's number:", nina_number)


# # 1.Create a tuple called dimensions with values 10, 20, 30. Unpack the values into variables 
# # length, width, and height, and print each variable.
# # 2.Given the tuple coordinates:
# # coordinates = (1.5, 2.5, 3.5)
# # Unpack the tuple into variables x, y, and z, and print the value of y.3.Create a tuple called
# # 3.person with values ("John", 25, "Engineer"). Unpack the values into variables name, age, and profession, and print the value of profession.
# # 4.Given the nested tuple data:
# # data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# # Unpack the first element of data into variables student1 and student2, and print student2.
# # 5.Create a tuple called colors with values ("red", "green", "blue", "yellow"). Unpack the first two values into variables color1 and color2, and print both variables.
# # 6.Given the tuple record:
# # record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# # Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. Print the extracted age and the first department.
# # 7.Create a tuple called triplet with values ("one", "two", "three"). Unpack the tuple into variables and print the value of the second variable.
# # 8.Given the tuple info:
# # info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# # Unpack the tuple to get the product ID, category, price, and manufacture date. Print the category and the manufacture year.
# #9. Create a tuple called nested_tuple with values (("a", "b"), ("c", "d"), ("e", "f")). Unpack the nested tuples into individual variables and print the second value of the third tuple.
# #10.Given the tuple inventory: inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# # Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas.


# # 1.Create a tuple called dimensions with values 10, 20, 30. Unpack the values into variables 
# # length, width, and height, and print each variable.
# dimensions =(10,20,30)
# length, width, height = dimensions
# print("length:",length)
# print("width:",width)
# print("height:",height)

# # 2.Given the tuple coordinates:
# # coordinates = (1.5, 2.5, 3.5)
# # Unpack the tuple into variables x, y, and z, and print the value of y.
# coordinates = (1.5, 2.5, 3.5)
# x, y, z =coordinates
# print("y:",y)

# # 3.create a tuple called person with values ("John", 25, "Engineer"). Unpack the values into variables name, age, and profession, and print the value of profession.
# person = ("John",25,"Engineer")
# name ,age ,profession = person
# print("profession:",profession)

# #4.Given the nested tuple data:
# # data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# # Unpack the first element of data into variables student1 and student2, and print student2.

# data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# student1,student2 =data[0]
# print("student2:",student2)

# # 5.Create a tuple called colors with values ("red", "green", "blue", "yellow"). Unpack the first two values into variables color1 and color2, and print both variables.
# colors = ("red", "green", "blue", "yellow")
# color1, color2 ,_ ,_ = colors
# print("color 1:",color1)
# print("color 2:",color2)

# # 6.Given the tuple record:
# # record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# # Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. Print the extracted age and the first department.
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, (age, position), (dept1,dept2) = record
# print(age)
# print(dept1)

# # 7.Create a tuple called triplet with values ("one", "two", "three"). Unpack the tuple into variables and print the value of the second variable.
# triplet = ("one", "two", "three")
# first, second , third = triplet
# print("Second:",second)

# # 8.Given the tuple info:
# # # info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# # # Unpack the tuple to get the product ID, category, price, and manufacture date. Print the category and the manufacture year.
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# product_id ,(categoy, price), (day,month,year) = info
# print("categoy:",categoy)
# print("Year:",year)

# #9.Create a tuple called nested_tuple with values (("a", "b"), ("c", "d"), ("e", "f")). Unpack the nested tuples into individual variables and print the second value of the third tuple.
# nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
# (first1, first2), (second1, second2), (third1, third2) = nested_tuple
# print(third2)

# #10.Given the tuple inventory: inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# # Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas.
# inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# (fruit1, qty1), (fruit2, qty2), (fruit3, qty3) = inventory
# print(f"bananas:{qty2}")


# # 1. Collect two numbers as input from the user and assign as variables, a and b, write an if 
# # statement that prints "a and b are both positive" if both a and b are positive, prints 
# # "Only one is positive" if one of them is positive, and prints "Neither is positive" if 
# # neither is positive.

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a > 0 and b > 0:
#     print("a and b are both positive")
# elif (a > 0 and b <= 0) or (a <= 0 and b > 0):
#     print("Only one is positive")
# else:
#     print("Neither is positive")


# #2.Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.
# x, y, z = input("Enter three numbers separated by commas: ").split(",")
# x, y, z = int(x), int(y), int(z)
# if x > y > z:
#     print("Increasing order")
# elif x > y > z:
#     print("Decreasing order")
# else:
#     print("Neither")


#  # 3.Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".
# palindrome = input("Enter a palindrome: ")
# if palindrome == palindrome[::-1]:
#     print("it is a palindrome")
# else:
#     print("Not a palindrome")


# #4.You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. Otherwise, print "All different" or "All same" accordingly.
# x = input("Enter first value: ")
# y = input("Enter second value: ")
# z = input("Enter third value: ")

# if x == y == z:
#     print("All same")
# elif x == y or y == z or x == z:
#     print("Two are equal")
# else:
#     print("All different")


# #5. Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements to check if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".
# angle1 = float(input("Enter first angle: "))
# angle2 = float(input("Enter second angle: "))
# angle3 = float(input("Enter third angle: "))

# if (angle1 + angle2 + angle3 == 180) and(angle1 > 0 and angle2 > 0 and angle3 > 0):
#     print("Valid triangle")
# else:
#     print("invalid triangle")

#  # 6.You have a single character variable `ch` supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that the input is a single alphabet character.
# ch = input("Enter a single alphabet character: ").strip()
# if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
#     print("Vowel")
# else:
#     print("Consonant")

# #7.Given a comma separated string input from the user of three colors color1, color2, and color3, write an if statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".
# color1, color2, color3 = input("Enter three colors separated by commas: ").split(",")
# color1 = color1.strip().lower()
# color2 = color2.strip().lower()
# color3 = color3.strip().lower()

# primary_colors = {"red", "blue", "yellow"}
# if color1 in primary_colors and color2 in primary_colors and color3 in primary_colors:
#     print("All primary colors")
# else:
#     print("Not all primary colors")


# #8.You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".
# mode = input("Enter mode (manual, automatic, off): ").strip().lower()
# if mode == "manual":
#     print("Manual mode activated")
# elif mode == "automatic":
#     print("Automatic mode activated")
# elif mode == "off":
#     print("System is off")
# else:
#     print("Invalid mode")


# #9.Given a string `message` entered by the user, use if statements to check if the message contains any of the words "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".
# message = input("Enter your message: ").lower().strip()
# if "urgent" in message or "important" in message or "immediate" in message:
#     print("High priority message")
# else:
#     print("Normal message")


# # 10.You have two variables, status1 and status2, provided through user input, each of 
# # 	which can be "active", “inactive", or "pending". Write an if statement to print 
# # 	"Both active" if both statuses are "active", "One active" if exactly one is "active",
# # 	and "None active" if neither is "active".

# status1 = input("Enter first status (active/inactive/pending): ").strip().lower()
# status2 = input("Enter second status (active/inactive/pending): ").strip().lower()

# if status1 == "active" and status2 == "active":
#     print("Both active")
# elif (status1 == "active" and status2 != "active") or (status1 != "active" and status2 == "active"):
#     print("One active")
# else:
#     print("None active")

# #11 Given a string `filename` supplied by the user, write an if statement to check if the
# 	# filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise
# 	# print "Not an image file".

# filename = input("Enter filename: ").strip().lower()
# if filename.endswith((".jpg", ".png", ".gif")):
#     print("Image file")
# else:
#     print("Not an image file")

# #12.You have a variable `access_level` provided through user input which can be "admin",
# 	# "user", or "guest". Write an if statement that prints "Full access" if access_level is
# 	# "admin", "Limited access" if it is "user", and "No access" if it is "guest".

# acces_level = input("Enter access level (admin/user/guest): ").strip().lower() 
# if acces_level == "admin":
#      print("Full access")
# elif acces_level == "user":
#     print("Limited access")
# elif acces_level == "guest":
#     print("No access")
# else:
#     print("Invalid access level")
# #13.Given a string `email` collected from the user, write an if statement to check if the
# # 	email contains both "@" and "." characters. Print "Valid email" if it does, otherwise
# # 	print "Invalid email".

# email = input("Enter your email: ").strip().lower()
# if "@" in email and "." in email:
#     print("Valid email")
# else:
#     print("Invalid email")

# #14.You have a variable `day` provided by user input which can be any day of the week 
# 	# (e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the
# 	# day is "Saturday" or "Sunday", and "Weekday" if it is any other day.
# day = input("Enter  any day of the week: ").strip().capitalize()
# if day == "saturday" or day == "Sunday":
#   print("weekend")
# else: 
#     print("Weekday")


# #15. Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 
# # 	input from the user and prints the greatest number. Use conditional statements
# # 	to determine which number is the greatest. Bonus point if you can do it without `else` 
# # 	statements.

# nums = input("Enter three numbers separated by commas: ")
# num1, num2, num3 = map(int, nums.split(","))
# greatest = num1  
# if num2 > greatest:
#     greatest = num2
# if num3 > greatest:
#     greatest = num3
# print("The greatest number is:", greatest)


# # for_loops classwork for 4th of september
#     # bodies_of_water = ["stream", "ocean", "river", "lagoon", "sea", "lake", "pond"]
# # filtered = [water for water in bodies_of_water if water != "river"]
# # print(filtered)

# # length_check = [len(water) <= 5 for water in bodies_of_water]
# # print(length_check)


# # things_that_move_in_the_air = {
# #     "birds": 1,
# #     "rocket": 1,
# #     "aeroplane": 2,
# #     "witches": 1,
# #     "chopper": 1,
# #     "jet": 1,
# #     "drone": 1
# # }
 

# #  # 1. Create a list of the square of each number
# # # Input: [1, 2, 3, 4, 5]
# # # Expected Output: [1, 4, 9, 16, 25]
# # digits = [1, 2, 3, 4, 5]
# # squares = [x**2 for x in digits]
# # print(squares)


# # # 2. Create a list of names that contain the letter 'a'
# # # Input: ["John", "Sara", "Mike", "Amanda"]
# # # Expected Output: ["Sara", "Amanda"]
# # names = ["John", "Sara", "Mike", "Amanda"]
# # names_with_a = [name for name in names if "a" in name.lower()]
# # print(names_with_a)


# # # 3. Create a list of Booleans indicating if each number is greater than 10
# # # Input: [5, 12, 3, 18, 7]
# # # Expected Output: [False, True, False, True, False]
# # values = [5, 12, 3, 18, 7]
# # greater_than_10 = [x > 10 for x in values]
# # print(greater_than_10)


# # # 4. Create a list of the last characters of each word
# # # Input: ["dog", "cat", "lion", "tiger"]
# # # Expected Output: ["g", "t", "n", "r"]
# # animals = ["dog", "cat", "lion", "tiger"]
# # last_chars = [animal[-1] for animal in animals]
# # print(last_chars) 

# # # 5. Are all the numbers greater than 10?
# # # Input: [5, 12, 3, 18, 7]
# # # Expected Output: False
# # values = [5, 12, 3, 18, 7]
# # all_greater = all(x > 10 for x in values)
# # print(all_greater)  


# # # 6. Is there any name that contains the letter 'a'?
# # # Input: ["John", "Sara", "Mike", "Amanda"]
# # # Expected Output: True
# # names = ["John", "Sara", "Mike", "Amanda"]
# # any_with_a = any("a" in name.lower() for name in names)
# # print(any_with_a)

# # #7.Get only the numbers that are divisible by 3 between 12 and 52
# # divisible_by_3 = [x for x in range(12, 53) if x % 3 == 0]
# # print(divisible_by_3)



# # 7. Are all the words made up of only uppercase letters?
# # # Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# # # Expected Output: False
# # greetings = ["HELLO", "world", "pyTHon", "ROCKS"]

# greetings = ["HELLO", "world", "pyTHon", "ROCKS"]
# result = all(word.isupper() for word in greetings)
# print(result)

# # 8. Is there any word that starts with 'z'?
# # # Input: ["apple", "zebra", "mango", "lemon"]
# # # Expected Output: True
# # words = ["apple", "zebra", "mango", "lemon"]

# words = ["apple", "zebra", "mango", "lemon"]
# result = any(word.startswith("z") for word in words)
# print(result)

# # # 9. Is there any email address that contains ".org"?
# # # Input: ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# # # Expected Output: True
# # emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]

# emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# result = any(".org" in email for email in emails)
# print(result)

# # # 10. Are all numbers odd?
# # # Input: [1, 3, 5, 7, 9]
# # # Expected Output: True
# # values = [1, 3, 5, 7, 9] 
# values = [1, 3, 5, 7, 9]
# are_all_odd = all(num % 2 != 0 for num in values)
# print(are_all_odd)


# # # 11. Are all words longer than 2 characters?
# # # Input: ["hi", "dog", "go", "sun"]
# # # Expected Output: False
# # words = ["hi", "dog", "go", "sun"]
# words = ["hi", "dog", "go", "sun"]
# result = all(len(word) > 2 for word in words)
# print(result)


# # 12. Create a list of triple the value of each number
# # # Input: [2, 4, 6, 8]
# # # Expected Output: [6, 12, 18, 24]
# # nums = [2, 4, 6, 8]
# nums = [2, 4, 6, 8]
# tripled = [num * 3 for num in nums]
# print(tripled)


# # # 13. Are all temperatures above 0°C?
# # # Input: [12, 7, 3, -1, 5]
# # # Expected Output: False
# # temperatures = [12, 7, 3, -1, 5]
# temperatures = [12, 7, 3, -1, 5]
# result = all( temp  > 0  for temp in temperatures)
# print(result)


# # # 14. Do all words end with a vowel?
# # # Input: ["banana", "mango", "kiwi", "grape"]
# # # Expected Output: True
# # fruits = ["banana", "mango", "kiwi", "grape"]
# fruits = ["banana", "mango", "kiwi", "grape"]
# vowels = ("a", "e", "i", "o", "u")
# result = all(word.endswith(vowels) for word in fruits)
# print(result)


# # # 15. Create a list of words in lowercase
# # # Input: ["HELLO", "WORLD", "PYTHON"]
# # # Expected Output: ["hello", "world", "python"]
# # greetings = ["HELLO", "WORLD", "PYTHON"]
# # greetings = ["HELLO", "WORLD", "PYTHON"]
# # result = [word.lower() for word in greetings]
# # print(result)


# # 16. Is there any number less than 0?
# # # Input: [5, -2, 3, 0, 8]
# # # Expected Output: True
# # numbers = [5, -2, 3, 0, 8]
# numbers = [5, -2, 3, 0, 8]
# result = any(num < 0 for num in numbers)

# # # 17. Create a list of words that contain the letter 'e'
# # # Input: ["sky", "tree", "rock", "stone"]
# # # Expected Output: ["tree", "stone"]
# # items = ["sky", "tree", "rock", "stone"]
# items = ["sky", "tree", "rock", "stone"]
# words_with_e =[item for item in items if "e" in item]
# print(words_with_e)


# # # 18. Are all names starting with uppercase letters?
# # # Input: ["Alice", "Bob", "charlie", "David"]
# # # Expected Output: False
# # names = ["Alice", "Bob", "charlie", "David"]
# names = ["Alice", "Bob", "charlie", "David"]
# result = all(name[0].isupper() for name in names)
# print(result)

# # # 19. Is there any sentence longer than 20 characters?
# # # Input: ["Short one", "This is a much longer sentence", "Okay"]
# # # Expected Output: True
# # sentences = ["Short one", "This is a much longer sentence", "Okay"]
# sentences = ["Short one", "This is a much longer sentence", "Okay"]
# any_sentence_longer_than_20 = any(len(sentence) > 20 for sentence in sentences)
# print(any_sentence_longer_than_20)

# # FUNCTIONS ASSIGNMENT.

# # 5. Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.
# def lesser_of_two_evens(a, b):
#     if a % 2 == 0 and b % 2 == 0:  
#         return min(a, b)           
#     else:                          
#         return max(a, b)           
# print(lesser_of_two_evens(2, 4))   
# print(lesser_of_two_evens(2, 5))   
# print(lesser_of_two_evens(7, 3))   
# print(lesser_of_two_evens(10, 15)) 

# # 6. Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter.
# # is_alliteration(‘Levelheaded llama’) —> True
# # is_alliteration(‘Crazy Kangaroo’) –> False 
# def is_alliteration(two_word_string: str):
#     words = two_word_string.lower().split()
#     word1, word2 = words
#     return word1[0] == word2[0]
    
# print(is_alliteration('Levelheaded llama')) # True
# print(is_alliteration('Crazy Kangaroo')) # False

# # 7. Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name
# # old_macdonald(‘macdonald’) —> MacDonald
# # Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.
# def old_macdonald(name):
#     if len(name) < 4:
#         return "Name must have at least 4 letters."
#     return name[:1].upper() + name[1:3] + name[3].upper() + name[4:]
# print(old_macdonald("macdonald"))      
# print(old_macdonald("Joy"))        

# # 8. Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.
# # spy_game([1, 2, 4, 0, 0, 7, 5]) —> True
# # spy_game([1, 0, 2, 4, 0, 5, 7]) —> True
# # spy_game([1, 7, 2, 0, 4, 5, 0]) —> False
# def spy_game(list_of_ints):
#     code = [0, 0, 7]
#     code_index = 0
    
#     for num in list_of_ints:
#         if num == code[code_index]:
#             code_index += 1
#             if code_index == len(code):  
#                 return True
#     return False
# print(spy_game([1, 2, 4, 0, 0, 7, 5]))  
# print(spy_game([1, 0, 2, 4, 0, 5, 7]))  
# print(spy_game([1, 7, 2, 0, 4, 5, 0]))   

# def filter_list(list_of_ints):
#     for list_of_ints in list_of_ints:
#         list_of_ints = [0,0,7]
#         list_of_ints.pop()

# # 9. Write a function vol(radius) that computes the volume of a sphere given its radius.
# import math

# def vol(radius):
#     return (4/3) * math.pi * (radius ** 3)
# print(vol(1))   
# print(vol(2))   
# print(vol(3))   

# #10. Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).
# def range_check(num, low, high):
#     return low <= num <= high
# print(range_check(5, 2, 7))   
# print(range_check(1, 2, 7))   
# print(range_check(7, 2, 7))   

# #11. Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.
# def upper_lower(text):
#     upper_count = 0
#     lower_count = 0
    
#     for char in text:
#         if char.isupper():
#             upper_count += 1
#         elif char.islower():
#             lower_count += 1
    
#     return {"Uppercase": upper_count, "Lowercase": lower_count}

# #12. Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.
# def unique_list(list_items):
#     unique = []
#     for item in list_items:
#         if item not in unique:
#             unique.append(item)
#     return unique
# print(unique_list(["apple", "pineapple", "apple", "orange", "pineapple"]))
# # 13.Write a function multiply(list_items) to multiply all the numbers in a list.
# # Sample List: [1, 2, 3, -4]
# # Expected output: -24 
# def multiply(list_items):
#     result = 1
#     for item in list_items:
#         result *= item
#     return result
# print(multiply([1, 2, 3, -4]))
# # 14. Write a function is_pangram(text) to check whether a string is a pangram or not. 
# # Note: A pangram is a word or sentence that contains every letter of the alphabet at  
# # least once. For example: “The quick brown fox jumps over the lazy dog”.
# # Hint: Import and use the string module.

# import string

# def is_pangram(text):
#     alphabet = set(string.ascii_lowercase)
#     return alphabet <= set(text.lower())
# print(is_pangram("The quick brown fox jumps over the lazy dog"))  
# print(is_pangram("Hello World"))  

# # 15. Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each
# # other. a word, phrase, or name formed by rearranging the letters of another, such as
# # spar, formed from rasp.
# def are_anagrams(s1, s2):
#     s1 = s1.replace(" ", "").lower()
#     s2 = s2.replace(" ", "").lower()
#     return sorted(s1) == sorted(s2)
# print(are_anagrams("spar", "rasp")) 

# # 16. Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# # (BMI) given weight in kilograms and height in meters.
# # 17. Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# # simple interest given principal amount, interest rate, and time (in years).

# class Car:
#     def  __init__(self,brand,model,year,horsepower,fuel_type):
#         self.brand = brand
#         self.model = model
#         self.horsepower = horsepower
#         self.fuel_type = fuel_type
#     def method(self):
#         return f"This is a {self.year} {self.brand} {self.model} with {self.horsepower} HP running on {self.fuel_type}"
    
# venza = Car( "Toyota","venza",2025,"50,000Km/h","Petrol")
# civic = Car( "Honda","Honda",2026,"40,000Km/h","Petrol")

# print(venza.fuel_type)
# print(civic.model)

# # 2. Create a class called Car with the following attributes:
# # #    - brand
# #    - model
# #    - year
# #    - horsepower
# #    - fuel_type
# #
# #    The class should have a method called car_info() that returns:
# #    "This is a {year} {brand} {model} with {horsepower} HP running on {fuel_type}."
# #
# #    After defining the class, create 3 different Car objects with different values.
# class Car:
#     def   __init__(self,brand,model,year,horsepower,fuel_type):
#         self.brand = brand
#         self.model = model
#         self.horsepower = horsepower
#         self.fuel_type = fuel_type
#     def method(self):
#         return f"This is a {self.year} {self.brand} {self.model} with {self.horsepower} HP running on {self.fuel_type}"
    
 
#     def __str__(self):
#         return self.brand
# venza = Car( "Toyota","venza",2025,"132","Petrol")
# civic = Car( "Honda","civic",2026,"630","Petrol")
# cybertruck = Car("Tesla", "cybertruck", 2022, 670, "Electric")

# print(venza.fuel_type)
# print(civic.brand)
# print(cybertruck.fuel_type)

# print(venza)


# # 3. Create a class called Student with the following attributes:
# #    - name
# #    - age
# #    - grades (a list of integers)
# #
# #    The class should have two methods:
# #    - average_grade(): returns the average of all grades
# #    - is_passing(): returns True if the average grade is >= 50, otherwise False
# #
# #    After defining the class, create 2 different Student objects with different values.

# # Example usage:
# # s1 = Student("Alice", 20, [60, 75, 80, 90])
# # s2 = Student("Bob", 19, [30, 40, 20, 45])

# # print(s1.name, "average:", s1.average_grade(), "passing:", s1.is_passing())
# # print(s2.name, "average:", s2.average_grade(), "passing:", s2.is_passing())

# # Expected Output:
# # Alice average: 76.25 passing: True
# # Bob average: 33.75 passing: False

# # class Student:
# #     def __init__(self, name, age, grades):
# #         self.name = name
# #         self.age = age
# #         self.grades = grades

# #     def average_grade(self):
# #         return sum(self.grades) / len(self.grades)

# #     def is_passing(self):
# #         return self.average_grade() >= 50


# # # Example usage:
# # s1 = Student("Ayomide", 20, [60, 75, 80, 90])
# # s2 = Student("John", 19, [30, 40, 20, 45])

# # print(s1.name, "average:", s1.average_grade(), "passing:", s1.is_passing())
# # print(s2.name, "average:", s2.average_grade(), "passing:", s2.is_passing())


# # 4. Create a class called Playlist with the following attributes:
# #    - name
# #    - songs (a list of strings)
# #
# #    The class should have three methods:
# #    - add_song(song): adds a new song title to the playlist
# #    - total_songs(): returns the total number of songs
# #    - show_songs(): returns all song titles as a comma-separated string
# #
# #    After defining the class, create a Playlist and add a few songs.

# # Example usage:
# # pl = Playlist("Workout Jams", ["Eye of the Tiger", "Stronger"])
# # pl.add_song("Lose Yourself")
# # pl.add_song("Can't Hold Us")

# # print(pl.name, "has", pl.total_songs(), "songs")
# # print("Songs:", pl.show_songs())

# # Expected Output:
# # Workout Jams has 4 songs
# # Songs: Eye of the Tiger, Stronger, Lose Yourself, Can't Hold Us
# # class Playlist:
# #     def __init__(self, name, songs=None):
# #         self.name = name
# #         self.songs = songs if songs else []

# #     def add_song(self, song):
# #         self.songs.append(song)

# #     def total_songs(self):
# #         return len(self.songs)

# #     def show_songs(self):
# #         return ", ".join(self.songs)


# # # Example usage
# # pl = Playlist("Workout Jams", ["Eye of the Tiger", "Stronger"])
# # pl.add_song("Lose Yourself")
# # pl.add_song("Can't Hold Us")

# # print(pl.name, "has", pl.total_songs(), "songs")
# # print("Songs:", pl.show_songs())


# # 5. Create a class called ShoppingCart with the following attributes:
# #    - owner
# #    - items (a dictionary where keys are item names and values are prices)
# #
# #    The class should have three methods:
# #    - add_item(item, price): adds the item with its price
# #    - total_cost(): returns the sum of all prices
# #    - most_expensive(): returns the item with the highest price
# #
# #    After defining the class, create a ShoppingCart and add multiple items.

# # Example usage:
# # cart = ShoppingCart("Alice", {})
# # cart.add_item("Laptop", 1200)
# # cart.add_item("Mouse", 25)
# # cart.add_item("Keyboard", 100)
# # cart.add_item("Monitor", 300)

# # print("Total cost:", cart.total_cost())
# # print("Most expensive item:", cart.most_expensive())

# # Expected Output:
# # Total cost: 1625
# # Most expensive item: Laptop

# # class ShoppingCart:
# #     def __init__(self, owner, items=None):
# #         self.owner = owner
# #         self.items = items if items else {}   

# #     def add_item(self, item, price):
# #         self.items[item] = price

# #     def total_cost(self):
# #         return sum(self.items.values())

# #     def most_expensive(self):
# #         if not self.items:   
# #             return None
# #         return max(self.items, key=self.items.get)


# # Example usage
# # cart = ShoppingCart("Alice")
# # cart.add_item("Laptop", 1200)
# # cart.add_item("Mouse", 25)
# # cart.add_item("Keyboard", 100)
# # cart.add_item("Monitor", 300)

# # print("Total cost:", cart.total_cost())
# # print("Most expensive item:", cart.most_expensive())

# class Book:
#     def __init__(self,title: str, pages: int,author):
#         self.title = title
#         self.pages = pages
#         self.author = author


# class library:
#     def __init__(self,list_of_books:list[Book]):
#         self.list_of_books = list_of_books

#     def total_pages(self):
#         return sum(book.pages for book in self.list_of_books)
    
# book1 = Book("Things Fall Apart","Chinua Achebe", 300)
# book2 = Book("Purple Hibiscus","Chinua Achebe", 300)

# OOP ASSIGNMENTS
# Fill in the Line class methods to accept coordinates as a pair of tuples and 
# return the slope and distance of the line. Look up the formulas for finding the distance and slope of a line.

import math
class Line:
    def __init__(self, coor1, coor2): 
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        distance = math.sqrt(((self.coor2[0]- self.coor1[0])**2) + ((self.coor2[1])- self.coor1[1])**2)
        return distance
    def slope(self):
        slope = (self.coor2[1]- self.coor1[1])/ (self.coor2[0]- self.coor1[0])
        return slope

        
# EXAMPLE EXECUTION

coordinate1 = (3,2)
coordinate2 = (8,10)

line_1 = Line(coordinate1, coordinate2)

print(line_1.distance())  # 9.433981132056603
print(line_1.slope())  # 1.6


# Fill in the class

class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume (self):
        return math.pi * self.radius ** 2 * self.height

    def surface_area(self):
        return 2 * math.pi * self.radius * (self.radius + self.height)

# EXAMPLE EXECUTION

cylinder = Cylinder(2,3)
print(cylinder.volume())  # 56.52
print(cylinder.surface_area())  # 94.2


# Scenario: You want to create a bank account that supports deposits and withdrawals.

# Task: Create a bank account class that has two attributes:

# owner
# balance

# and two methods:
# deposit
# Withdraw

# Withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account 
# can't be overdrawn.

# You are not expected to use the input function, just pass in values for the amounts into 
# the methods directly, no need for loops either.

# See the next slide for a sample execution of the code you will write.
class Account: 
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print("Deposit Accepted")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Accepted")
        else:
            print("Funds Unavailable!")
    
    def __str__(self):
        return f"Account owner: {self.owner}\nAccount balance: ${self.balance}"


    

#1. Instantiate the class
acct1 = Account('Winnie', 100)

#2. Print the object
print(acct1)
# Output:
# Account owner: Winnie
# Account balance: $100

#3. Show the account owner attribute
print(acct1.owner)  # Winnie

#4. Show the account balance attribute 
print(acct1.balance)  # 100

#5. Make a series of deposits and withdrawals 
acct1.deposit(50)  # Output: Deposit Accepted

acct1.withdraw(15)  # Output: Withdrawal Accepted

#6. Make a withdrawal that exceeds the available balance 
acct1.withdraw(500)  # Output: Funds Unavailable!


# ===========================
# Assignment Exercises
# ===========================

# Each exercise describes a scenario with classes, objects, and interactions.  
# Your task: implement the classes and methods so that the given sample execution works  
# and produces the expected output.

# -----------------------------------------------------------
# 1. Library & Borrowing
# -----------------------------------------------------------
# book1 = Book("1984", "George Orwell", 5)
# book2 = Book("Brave New World", "Aldous Huxley", 2)

# library = Library([book1, book2])

# print(library.borrow("1984"))
# # -> True

# print(library.borrow("Brave New World"))
# # -> True

# print(library.borrow("Brave New World"))
# # -> True

# print(library.borrow("Brave New World"))
# # -> False

# print(library.available_books())
# # -> {'1984': 4, 'Brave New World': 0}
class Book:
    def __init__(self,title,author,quantity):
        self.title = title
        self.author = author
        self.quantity = quantity 
class Library:
    def __init__(self,books):
        self.books = {}
        for book in books:
            self.books[book.title] = book.quantity 
    def borrow(self,title):
        if title in self.books and self.books[title]> 0:
            self.books[title] -= 1
            return True
        return  False
    def available_books(self):
        return self.books
    
book1 = Book("1984", "George Orwell", 5)
book2 = Book("Brave New World", "Aldous Huxley", 2)
library = Library([book1, book2])

print(library.borrow("1984"))
# -> True
print(library.borrow("Brave New World"))
# -> True
print(library.borrow("Brave New World"))
# -> True
print(library.borrow("Brave New World"))
# -> False
print(library.available_books())
# -> {'1984': 4, 'Brave New World': 0}


# -----------------------------------------------------------
# 2. Shopping Cart with Discounts
# -----------------------------------------------------------
# cart = ShoppingCart()

# cart.add_item("milk", 500, 2)
# cart.add_item("bread", 1000, 1)

# print(cart.total())
# # -> 2000

# cart.apply_discount(10)   # 10% discount
# print(cart.total())
# # -> 1800


# -----------------------------------------------------------
# 3. Cinema Ticket Booking (with user input)
# -----------------------------------------------------------
# # Assume input:
# # Enter movie name: Interstellar
# # Enter seats to book: 3

# cinema = Cinema({"Interstellar": 5, "Inception": 2})

# movie = input("Enter movie name: ").strip()
# seats = int(input("Enter seats to book: "))

# print(cinema.book(movie, seats))
# # If user entered "Interstellar" and "3"
# # -> True

# print(cinema.show_available())
# # -> {'Interstellar': 2, 'Inception': 2}
class Cinema:
    def __init__(self, movies):
        self.movies = movies
    def book(self, movie, seats):
        if movie in self.movies:
            if self.movies[movie] >= seats:
                self.movies[movie] -= seats
                return True
            else:
                return 
        return False
    def show_available(self):
        return self.movies 
    
cinema = Cinema({"Interstellar": 5, "Inception": 2})
movie = input("Enter movie name: ").strip()
seats = int(input("Enter seats to book: "))
print(cinema.book(movie, seats))
print(cinema.show_available())

# -----------------------------------------------------------
# 4. Student Grades & Average
# -----------------------------------------------------------
# course1 = Course("Math", 80)
# course2 = Course("Physics", 70)
# course3 = Course("English", 90)

# student = Student("Amina", [course1, course2, course3])

# print(student.average())
# # -> 80.0

# print(student.best_course())
# # -> English