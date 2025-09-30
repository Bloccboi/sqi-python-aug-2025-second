#                  MUTABLE               INDEXED           ORDERED             ALLOWS DUPLICATES
# List              Yes                    Yes               Yes                        Yes
# Tuple             No                     Yes               Yes                        Yes
# Set               Yes                    No                No                         No
# Dictionaries      Yes              Yes, but with keys Yes (but in recent versions)    Allow duplicate values, but not duplicate keys




# praise = {"name": "Akande Praise", "age": 12, "is_male": True, "complexion": "light"}

# praise = ["Akande Praise", 12, True, "light"]

# phone_book = {"Sam": "08025538654", "Ife": "08169762937", "Damilola": "07063457615", 0:"zero"}

# print(phone_book["Ife"])
# print(phone_book["Damilola"])
# print(phone_book[0])
# print(phone_book)


# praise = {"name": "Akande Praise", "age": 12, "favorite_num": 12, "is_male": True, "name": "Olawumi Ayomide", "complexion": "light"}
# print(praise)

# phone_book = {"Sam": "08025538654", "Ife": "08169762937", "Damilola": "07063457615", 0:"zero"}
# phone_book["Damilola"] = "07063457610"
# print(phone_book)
# phone
# print(phone_book)

# phone_book["Sam"] = "08012378000"
# print(phone_book)

# phone_book = {"Sam": "08025538654", "Ife": "08169762937", "Damilola": "07063457615", 0:"zero"}



# phone_book = {"Sam": "08025538654", "Ife": "08169762937", "Damilola": "07063457615"}
# # del phone_book["tefv3dbhnxje3k"]  # keyError
# del phone_book["Damilola"]  # keyError
# print(phone_book)

# phone_book = {"Sam": "08025538654", "Ife": "08169762937", "Damilola": "07063457615"}
# print("Ife" in phone_book)



# phone_book = {"Sam": "08025538654", "Ife": "08169762937", "Damilola": "07063457615"}
# print(phone_book.keys())  # dict_keys
# print(list(phone_book.keys())[0])  # Sam

# print(phone_book.values())  # dict_values
# print(list(phone_book.values())[1])  # dict_values

# print(phone_book.items())  # dict_items - looks like a list of tuples where tuple[0] is the key, and tuple[1] is the 

# print("08169762937" in phone_book.values())


# phone_book = [
#     {"name": "Sam", "phone": "08025538654"},
#     {"name": "Sam", "phone": "08021238634"}
# ]
# print(phone_book[0]["phone"])
# print(phone_book[1]["phone"])

# phone_book = {"Sam": ["08025538654", "08021238634"], "Ife": ["08169762937", "09030556519"], "Damilola": ["07063457615", "0908906723"]}
# print(phone_book["Sam"][1])



# yoruba_translator = {
#     "book": "iwe",
#     "snake": "ejo",
#     "tree": "igi",
#     "shoe": "bata",
#     "broom": "igbale",
#     "get_up": "dide"
# }

# print(yoruba_translator["snake"])
# print(yoruba_translator["get_up"])





# Create a dictionary called student with the following keys: 
# "full_name", "age", "dept", "current_level", "gpa", "course", "is_full_time"
# provide values for the keys and do the following:
# 1. Add a new key "matric_no" with a value to the student dict
# 2. Change the value of the "gpa" key to 5.0
# 3. Remove the age from the student dict
# 4. Check if "dept" is in the dict
# 5. Check if "Data Science" is a value in the dict
# 6. Print out a LIST of the keys of the dict
# 7. Print out the first value in the dict without using the key "full_name"


# student = {"full_name": "Maryam Aleshinloye", "age": 29, "dept": "Artificial Intelligence", "current_level": "Python", "gpa": 4.5, "course": "Artificial Intelligence", "is_full_time": True}

# student["matric_no"] = "20256689"
# student["gpa"] = 5.0

# del student["age"]

# print("dept" in student)

# print("Data Science" in student.values())

# print(list(student.keys()))

# print(list(student.values())[0])


# student = {"full_name": "Maryam Aleshinloye", "age": 29, "dept": "Artificial Intelligence", "current_level": "Python", "gpa": 4.5, "course": "Artificial Intelligence", "is_full_time": True}

# print(student["dept"])
# print(student.get("dept"))

# print(student["department"])  # KeyError
# print(student.get("department"))  # None
# print(student.get("dept", "Does not exist"))
# print(student.get("department", "Does not exist"))


# student = {"full_name": "Maryam Aleshinloye", "age": 29, "dept": "Artificial Intelligence", "current_level": "Python", "gpa": 4.5, "course": "Artificial Intelligence", "is_full_time": True}

# print(student.setdefault("full_name"))
# print(student.setdefault("name"))
# print(student.setdefault("name", "Anonymous"))
# print(student)



# -------------------------------------UPDATE DICT----------------------------------------------
# Method 1: square bracket notation
# ife_dream_car = {
#     "brand": "Tesla",
#     "model": "Cybertruck",
#     "is_eletric": True,
#     "year": 2025
# }

# ife_dream_car["model"] = "Model X"
# ife_dream_car["color"] = "silver"

# print(ife_dream_car)


# Method 2: .update with dict

# ife_dream_car = {
#     "brand": "Tesla",
#     "model": "Cybertruck",
#     "is_eletric": True,
#     "year": 2025
# }
# ife_dream_car.update({'color': "silver"})
# ife_dream_car.update({'color': "silver", "year": 2000})
# ife_dream_car.update({'color': "silver", "year": 2000, "is fast": True})
# print(ife_dream_car)



# Method 3: .update with kwargs - keyword arguments
# ife_dream_car = {
#     "brand": "Tesla",
#     "model": "Cybertruck",
#     "is_eletric": True,
#     "year": 2025
# }

# ife_dream_car.update(color="silver", year=2000, is_fast=True)
# print(ife_dream_car)

# -------------------------------------UPDATE DICT----------------------------------------------



# -------------------------------------REMOVE FROM A DICT----------------------------------------------
# Method 1: using del keyword
# ife_dream_car = {
#     "brand": "Tesla",
#     "model": "Cybertruck",
#     "is_eletric": True,
#     "year": 2025
# }

# del ife_dream_car["is_eletric"]
# print(ife_dream_car)


# Method 2: using the .pop()
# ife_dream_car = {
#     "brand": "Tesla",
#     "model": "Cybertruck",
#     "is_eletric": True,
#     "year": 2025
# }

# popped = ife_dream_car.pop("is_eletric")
# print("popped:", popped)
# print(ife_dream_car)


# Method 3: using the .popitem()
# ife_dream_car = {
#     "brand": "Tesla",
#     "model": "Cybertruck",
#     "is_eletric": True,
#     "year": 2025
# }

# popped = ife_dream_car.popitem()
# print("popped:", popped)
# popped = ife_dream_car.popitem()
# print("popped:", popped)
# popped = ife_dream_car.popitem()
# print("popped:", popped)
# popped = ife_dream_car.popitem()
# print("popped:", popped)
# popped = ife_dream_car.popitem()
# print("popped:", popped)
# print(ife_dream_car)
# -------------------------------------REMOVE FROM A DICT----------------------------------------------





# ife_dream_car = {
#     "brand": "Tesla",
#     "model": "Cybertruck",
#     "is_eletric": True,
#     "year": 2025,
#     (12,3, 4): "etfdybhmkx",
#     123: "one hundred and twenty three",
# }
# print(len(ife_dream_car))
# print(type(ife_dream_car))


# my_list = [1, 2, 3, 4, 5]
# print(dict(my_list))
# my_data = [(1, "one"), (2, "two"), (3, "three"), (4, "four"), (5, "five")]
# my_data = [[1, "one"], [2, "two"], [3, "three"], [4, "four"], [5, "five"]]
# my_data = ([1, "one"], [2, "two"], [3, "three"], [4, "four"], [5, "five"])
# print(dict(my_data))


# my_data = dict(one=1, two=2, three=3, four=4, five=5)
# print(my_data)



# data = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
# data.clear()
# print(data)


# empty_dict = {}
# print(type(empty_dict))

# empty_set = set()
# print(type(empty_set))


# my_set = {}


# -------------------------------------COPY A DICT----------------------------------------------

# import copy

# sam_laptop = {
#     "brand": "Mac",
#     "ram": 8,
#     "manufacturer": "Apple",
#     "battery": 90,
#     "configuration": [8, 256]
# }

# # duplicate = sam_laptop.copy()
# duplicate = copy.deepcopy(sam_laptop)

# duplicate["configuration"][0] = 16

# print(sam_laptop)
# print(duplicate)

# -------------------------------------COPY A DICT----------------------------------------------


#1.Create a dictionary called `student` with keys "name", "age", and "grade", and corresponding values "John", 20, and "A". Access and print the value of "name".
student = {"name": "John", "age": 20, "grade":"A" }
print(student["name"])

#2.Create a dictionary called `product` with keys "name", "price", and "stock", and corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.
product = {"name": "Laptop", "price": 999.9 ,"stock": "50"}
product["price"] = 899.99
print(product)

#3.Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager". Add a new key "salary" with the value 50000.
employee = {"name":"Alice","position":"Manager"}
employee["salary"] = 50000
print(employee)

#4.Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively. Remove the key "banana".
inventory ={"apple":10,"banana":5,"orange":8}
del inventory["banana"]
print(inventory)

#5.Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York". Use the copy() method to make a copy of the dictionary and call it person_copy.
person = {"name":"Bob","age":25,"city":"New York"}
person_copy =person.copy
person = person.copy()
print("Original:", person)
print("Copy:",person_copy)


#6.Create a nested dictionary called `family` with keys "child1", "child2", and "child3", each containing a dictionary with keys "name" and "age" with appropriate values. Access and print the age of "child2".
family = {
    "child1": {"name":"labs" , "age":25},
    "child2": {"name":"Dolapo" ,"age":17},
    "child3": { "name":"Peace" ,"age":20}
}
print("The age of child2 is:", family["child2"]["age"])


#7.Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values "Toyota", "Corolla", and 2020. Access and print the value of "model".
car = {"brand": "Toyota", "model": "Corolla" , "year": 2020}
print(car["model"])


#8.Create a dictionary called `settings` with keys "volume", "brightness", and "language", and corresponding values 50, 75, and "English". Change the "language" to "Spanish".
settings = {"volume":50, "brightness":75 ,"language":"English"}
settings["language"]= "Spanish"
print(settings)


#9.Create a dictionary called `scores` with keys "math", "science", and "english", and corresponding values 90, 85, and 88. Remove the key "science".
scores = {"maths":90, "science":85 ,"english":88}
del scores["science"]
print(scores)


#10.Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", and corresponding values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer" is present in the dictionary.
menu = {"starter": "soup", "main_course": "steak", "dessert": "Ice Cream"}
print("appetizer" in menu)


#11.Create a dictionary called `config` with keys "theme", "language", and "timezone", and corresponding values "dark", "English", and "UTC". Clear the dictionary.
config = {"theme": "dark", "language": "English", "timezone" :"UTC"}
config.clear()
print(config)


#12.Create a dictionary called `phone_book` with keys "Alice", "Bob", and "Charlie", and corresponding phone numbers as values. Print the number of items in the dictionary.
phone_book = [
    { "name":"Alice", "phone":"08147882614" },
    { "name":"Bob", "phone":"08033809387" },
    { "name":"Charlie", "phone":"08035528191"}

]
print(len(phone_book))


#13.Create a dictionary called `grades` with keys "math", "science", and "history", 
# and corresponding values "A", "B", and "C". Get a LIST of all the keys in the 
# dictionary.
grades = {"math": "A","science": "B","history": "C"}
keys_list = list(grades.keys())
print(keys_list)


#14.Create a dictionary called `employee` with keys "name", "position", and "salary", and corresponding values "David", "Engineer", and 70000. Get a LIST  of all the values in the dictionary.
employee = {"name": "David", "position": "Engineer", "salary":"70000"}
values_list =list(employee.values())
print((values_list))


# 15.Create a dictionary called `game` with keys "title", "genre", and "rating", and corresponding values "Minecraft", "Sandbox", and 4.5. Get a LIST of all key-value pairs in the dictionary.
game = {"title":"Minecraft" ,"genre":"sandbox", "rating":4.5}
pairs_list = list(game.items())
print(pairs_list)


#  ===============================
# Nested Dictionary Modification Exercises
# ===============================

# Q1. Given this dictionary, change the "math" score to 95.
student = {
    "name": "Alice",
    "scores": {"math": 80, "english": 85}
}
student["scores"]["math"] = 95
print(student)


# Q2. Add a new subject "science" with score 90 inside "scores".
student = {
    "name": "Alice",
    "scores": {"math": 80, "english": 85}

}
student["scores"]["science"] = 90
print(student)
 

# Q3. Change the author's name of "Python 101" to "Mike".
library = {
    "Python 101": {"author": "Tom", "year": 2020},
    "Data Science": {"author": "Jane", "year": 2021}
}
library["Python 101"]["author"]= "Mike"
print(library)


# Q4. Add a new key "publisher" = "O'Reilly" to "Data Science".
library = {
    "Python 101": {"author": "Tom", "year": 2020},
    "Data Science": {"author": "Jane", "year": 2021}
}
library["Data Science"]["publisher"]= "O'Reilly"
print(library)


# Q5. In this dictionary, add a new phone number "work": "555-999" for Alice.
contacts = {
    "Alice": {"home": "555-123", "mobile": "555-456"},
    "Bob": {"home": "555-789"}
}
contacts["Alice"]["work"]= 555-999
print(contacts)


# Q6. Change Bob’s "home" number to "555-000".
contacts = {
    "Alice": {"home": "555-123", "mobile": "555-456"},
    "Bob": {"home": "555-789"}
}
contacts["Bob"]["home"]="555-000"
print(contacts)


# Q7. Add a new student {"name": "Eve", "scores": {"math": 88, "english": 92}}
# into the list of students.
students = [
    {"name": "Alice", "scores": {"math": 80, "english": 85}},
    {"name": "Bob", "scores": {"math": 75, "english": 70}}
]
new_students = {"name": "Eve", "scores": {"math": 88, "english": 92}} 
students.append (new_students)
print(students)


# Q8. Change Bob's english score from 70 to 78.
students = [
    {"name": "Alice", "scores": {"math": 80, "english": 85}},
    {"name": "Bob", "scores": {"math": 75, "english": 70}}
    
]
students[1]["scores"]["english"] =78
print(students)


# Q9. Add a new dictionary {"year": 2022, "semester": "Spring"} 
# inside Alice’s record under a new key "enrollment".
students = [
    {"name": "Alice", "scores": {"math": 80, "english": 85}},
    {"name": "Bob", "scores": {"math": 75, "english": 78}}
]
enrollment_info = {"year": 2022, "semester": "spring"}
students[0]["enrollment"] = enrollment_info
print(students)

# Q10. In this shop cart, add a new product "Notebook" with price 200.
cart = {
    "items": [
        {"name": "Pen", "price": 10},
        {"name": "Book", "price": 50}
    ],
    "owner": "Alice"
}
new_product = {"name": "Notebook", "price": 200}
cart["items"].append(new_product)
print(cart)
