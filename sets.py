# my_set = set()
# print(my_set)

# my_set = {}
# print(my_set)
# print(type(my_set))


# my_set = {1, 89, 5672, 682}
# print(my_set)
# print(type(my_set))




#                       STRINGS            LISTS            TUPLES              DICTS               SETS
# Ordered                 Yes               Yes               Yes               Yes                 No
# Indexed                 Yes               Yes               Yes               Yes, but with keys  No
# Mutable                  No               Yes               No                Yes                 Yes
# Allow duplicates        Yes               Yes               Yes               Allows duplicate    No
#                                                                               values but not keys

# my_set = {89, 678, 262}
# print(my_set[120])


# my_name = "Elizabeth"
# my_name[2] = "G"

# my_names = ["Winifred", "Chinaza", "Igboama"]
# my_names[1] = "Naza"
# print(my_names)

# items = ("bag", "shoe", "clothes", "glasses")
# items[1] = "shoes"


# Sets are unordered
# items = {"bag", "shoe", "clothes", "glasses"}
# print(items)

# items = {"bag", "shoe", "clothes", "glasses"}
# print(items[3])  # unindexed


# # items = {"bag", "shoe", "clothes", "bag", "glasses"}
# print(items)
# print(len(items))


# items = {"bag", "shoe", "clothes", "Bag", "glasses"}
# print(items)
# print(len(items))



# items = {"bag", "shoe", True, "clothes", "Bag", 1, "glasses"}
# print(items)


# items = {"bag", False, 0, "shoe", True, "clothes", "Bag", 1, "glasses"}
# print(items)

# items = ("bag", "shoe", "clothes", "glasses")
# print(set(items))

# items = ("bag", "shoe", "clothes", "glasses")
# items = set(items)
# print(items)


# items = ("bag", "shoe", "clothes", "shoe", "glasses", "shoe")

# items = set(items)

# items = tuple(items)
# print(items)



# name = "Damilola"
# name = set(name)
# name = "".join(name)
# print(name)


# -----------------------------------SET METHODS--------------------------------------------

# ========================ADDING TO A SET========================

# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# movies.add("Avengers: EndGame")
# print(movies)

# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# movies.update({"Black Panther", "Ghost Rider"})
# print(movies)
# movies.update(("Black Panther",))
# print(movies)


# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# other_movies = {"Black Panther", "Ghost Rider"}
# extra_movies = {"Heads of State", "Pentagon"}
# more_movies = {"White Collar", "Six Dragons"}
# all_movies = set()
# all_movies.update(movies)
# all_movies.update(other_movies)
# all_movies.update(extra_movies)
# all_movies.update(more_movies)


# print(movies)
# print(other_movies)
# print(extra_movies)
# print(more_movies)
# print(all_movies)

# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# other_movies = {"Black Panther", "Ghost Rider"}
# all_movies = movies.union(other_movies)
# # print(movies)
# print(other_movies)
# # print(all_movies)

# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# other_movies = ["Black Panther", "Ghost Rider"]
# extra_movies = ("Heads of State", "Pentagon")
# more_movies = ("White Collar", "Six Dragons")

# all_movies = movies.union(other_movies).union(extra_movies).union(more_movies)
# print(movies)
# print(other_movies)
# print(extra_movies)
# print(more_movies)
# print(all_movies)

# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# other_movies = {"Black Panther", "Ghost Rider"}
# extra_movies = {"Heads of State", "Pentagon"}
# more_movies = {"White Collar", "Six Dragons"}

# all_movies = movies.union(other_movies).union(extra_movies).union(more_movies)
# print(movies)
# print(other_movies)
# print(extra_movies)
# print(more_movies)
# print(all_movies)

# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# other_movies = {"Black Panther", "Ghost Rider"}
# all_movies = movies | other_movies
# print(movies)
# print(other_movies)
# print(all_movies)


# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# other_movies = {"Black Panther", "Ghost Rider"}
# extra_movies = {"Heads of State", "Pentagon"}
# more_movies = {"White Collar", "Six Dragons"}

# all_movies = movies | other_movies | extra_movies | more_movies
# print(movies)
# print(other_movies)
# print(extra_movies)
# print(more_movies)
# print(all_movies)


# movies = {"Fast and Furious", "Mission Impossible", "To Kill a Monkey", "Death Note", "Shaolin Soccer"}
# other_movies = ["Black Panther", "Ghost Rider"]
# extra_movies = ("Heads of State", "Pentagon")
# more_movies = {"White Collar", "Six Dragons"}

# all_movies = movies | other_movies | extra_movies | more_movies
# print(movies)
# print(other_movies)
# print(extra_movies)
# print(more_movies)
# print(all_movies)


# ========================ADDING TO A SET========================



# ========================INTERSECTION OF SETS========================

animes = {"Blue Lock", "JJK", "AOT"}
other_animes = {"Death Note", "One Piece"}
more_animes = {"Naruto", "Bleach"}

intersection = animes.intersection(other_animes).intersection(more_animes)

print(intersection)



# animes = {"Blue Lock", "JJK", "AOT"}
# other_animes = {"Death Note", "AOT", "One Piece"}
# # more_animes = {"Naruto", "AOT", "Bleach"}
# more_animes = {"Naruto", "Bleach"}

# intersection = animes.intersection(other_animes).intersection(more_animes)

# print(intersection)


# animes = {"Blue Lock", "JJK", "AOT"}
# other_animes = {"Death Note", "JJK", "AOT", "One Piece"}
# more_animes = {"Naruto", "JJK", "Bleach"}

# animes.intersection_update(animes)
# animes.intersection_update(other_animes)
# animes.intersection_update(more_animes)
# print(animes)


# animes = {"Blue Lock", "JJK", "AOT"}
# other_animes = {"Death Note", "JJK", "AOT", "One Piece"}
# more_animes = {"Naruto", "JJK", "Bleach"}
# intersection = animes & other_animes & more_animes
# print(intersection)


# animes = {"Blue Lock", "JJK", "AOT"}
# other_animes = ["Death Note", "JJK", "AOT", "One Piece"]
# more_animes = ("Naruto", "JJK", "Bleach")
# intersection = animes & other_animes & more_animes
# print(intersection)
# ========================INTERSECTION OF SETS========================




# ========================REMOVE FROM SETS========================

# fast_cars = {"Porsche", "Ferrari", "Buggati", "Lamborghini", "Dodge"}
# fast_cars.remove("Ferrari")
# print(fast_cars)

# fast_cars = ["Porsche", "Ferrari", "Buggati", "Lamborghini", "Dodge"]
# fast_cars.remove("Mustang")

# fast_cars = {"Porsche", "Ferrari", "Buggati", "Lamborghini", "Dodge"}
# fast_cars.remove("Mustang")
# print(fast_cars)

# fast_cars = {"Porsche", "Ferrari", "Buggati", "Lamborghini", "Dodge"}
# # fast_cars.discard("Ferrari")
# fast_cars.discard("Mustang")
# print(fast_cars)


# type annotation / type hint
# fast_cars: set[str | int] = {"Porsche", "Ferrari", "Buggati", "Lamborghini", "Dodge"}
# popped_car = fast_cars.pop()
# print(fast_cars)
# print(popped_car)

# fast_cars: set[str | int] = {"Porsche", "Ferrari", "Buggati", "Lamborghini", "Dodge"}
# fast_cars.clear()
# print(fast_cars)

# fast_cars: set[str | int] = {"Porsche", "Ferrari", "Buggati", "Lamborghini", "Dodge"}
# # del fast_cars[0]  # TypeError
# del fast_cars
# print(fast_cars)  # NameError


# Del keyword

# my_list = ["James", "John", "Jake", "Jerry"]
# # del my_list[2]
# del my_list
# print(my_list)  # NameError



# ========================.DIFFERENCE() METHOD========================

# # mobile_games = {"CODM", "PUBG", "Fortnite", "Angela", "Candy Crush", "One State", "Free Fire"}
# mobile_games = {"CODM", "PUBG", "Fortnite", "Candy Crush", "Free Fire"}
# more_mobile_games = {"DLS", "Angela", "Talking Tom", "One State", "Subway Surf"}
# # even_more_mobile_games = {"Delta Force", "Warzone", "E-Football", "FIFA"}

# difference = mobile_games.difference(more_mobile_games)

# print(difference)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# # set3 = set1.difference(set2)
# set3 = set1 - set2

# print(set3)


# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set1.difference_update(set2)
# print(set1)

# ========================.DIFFERENCE() METHOD========================


# ========================.SYMMETRIC_DIFFERENCE() METHOD========================
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)


# mobile_games = {"CODM", "PUBG", "Fortnite", "Angela", "Candy Crush", "One State", "Free Fire"}
# more_mobile_games = {"DLS", "Angela", "Talking Tom", "One State", "Subway Surf"}

# print(mobile_games.intersection(more_mobile_games))

# all_games = mobile_games | more_mobile_games
# intersection = mobile_games & more_mobile_games
# symmetric_diff = all_games - intersection
# print(symmetric_diff)

# symmetric_diff_2 = mobile_games.symmetric_difference(more_mobile_games)
# mobile_games.symmetric_difference_update(more_mobile_games)
# print(mobile_games)

# symmetric_diff_2 = mobile_games ^ more_mobile_games
# print(symmetric_diff_2)



# # even_more_mobile_games = {"Delta Force", "Warzone", "E-Football", "FIFA"}

# ========================.SYMMETRIC_DIFFERENCE() METHOD========================



# ========================MISCELLANEOUS========================


# more_mobile_games = {"DLS", "Angela", "Talking Tom", "One State", "Subway Surf"}
# even_more_mobile_games = {"Delta Force", "Warzone", "E-Football", "FIFA"}
# print(even_more_mobile_games.issubset(more_mobile_games))


# nums1 = {1, 2, 3, 4, 5, 6}
# nums2 = {2, 5, 1}
# print(nums2.issubset(nums1))
# print(nums2.issubset(nums2))

# nums1 = {1, 2, 3, 4, 5, 6}
# nums2 = {2, 5, 1}

# print(nums1.intersection(nums2))

# print(nums1.isdisjoint(nums2))
# nums1 = {1, 2, 3, 4, 5, 6}
# nums2 = {20, 15, 11}
# print(nums1.isdisjoint(nums2))





# ========================MISCELLANEOUS========================


# -----------------------------------SET METHODS--------------------------------------------


# ASS
#1.Create a set called fruits with values {"air", "water", "food"}. Check if "food" is in the set and print the result.
fruits = {"air", "water", "food"}
print("food" not in fruits)

#2.Create a set called colors with values {"red", "green", "blue"}. Add the color "yellow" to the set and print the updated set.
color = {"red", "green", "blue"}
color.add("yellow")
print(color)


#3.Given the set animals = {"cat", "dog", "rabbit"}, add multiple items ["horse", "sheep"] to the set and print the updated set.
animals = {"cat", "dog", "rabbit"}
more_animals ={"horse", "sheep"}
animals.update(more_animals)
print(animals)


#4.Create a set called countries with values {"USA", "Canada", "Mexico"}. Remove "Canada" from the set and print the updated set.
countries = {"USA", "Canada", "Mexico"} 
countries.remove("Canada")
print(countries)


#5.Given the set cities = {"New York", "Los Angeles", "Chicago"}, remove "Houston" which is not in the set without raising an error.
cities = {"New York", "Los Angeles", "Chicago"}
cities.discard("Houston")
print(cities)


#6.Given the list seasons = ["Spring", "Summer", "Fall", "Winter", “Spring”], convert the list to a set to get rid of the duplicate `Spring`.
seasons = ["Spring", "Summer", "Fall", "Winter", "Spring"]
new_seasons = set(seasons)
print(seasons)


#7.Create two sets, set1 = {1, 2, 3} and set2 = {3, 4, 5}. Use the union method to join the sets and print the result.
set1 ={1,2,3}
set2 ={3,4,5}
set3 = set1.union(set2)
print(set3)

#8.Given two sets, setA = {"a", "b", "c"} and setB = {"c", "d", "e"}, find the intersection of the sets and print the result.
setA = {"a", "b", "c"}
setB = {"c", "d", "e"}
setC = setA.intersection(setB)
print(setC)


#9.Create a set called prime_numbers with values {2, 3, 5, 7}. Add the number 11 to the set and print the updated set.
prime_numbers = {2,3,5,7}
prime_numbers.add(11)
print(prime_numbers)


#10.Given the set odd_numbers = {1, 3, 5, 7, 9}, remove a random item from the set and print the updated set.
odd_numbers = {1, 3, 5, 7, 9}
odd_numbers.pop()
print(odd_numbers)


#11.Create a set called vowels with values {"a", "e", "i", "o", "u"}. Empty the set and print the result.
vowels = {"a", "e", "i", "o", "u"}
vowels.clear()
print(vowels)


#12 Given the set letters = {"a", "b", "c"}, find the difference between `letters` and another set {"b", "c", "d"}. Print the result. Afterwards, find the symmetric difference and print the result.
letters = {"a", "b", "c"}
letters2= {"b", "c", "d"}
difference  = letters-letters2
print(difference)
sym_diff = letters ^ letters2
print(sym_diff)
#13.Create a set called tech_brands with values {"Apple", "Google", "Microsoft"}. 
# Add the items from another set {"Amazon", "Facebook"} and print the updated set 
# tech_brands without creating a new set.
tech_brands = {"Apple","Google","Microsoft"}
tech_brands.update({"Amazon","Facebook"})
print(tech_brands)


#14.Create a set called students with values {"Alice", "Bob", "Charlie", "David"}. Use the 
#remove method to remove "Charlie" from the set and print the updated set. Then try to 
#remove "Eve" from the set and observe the behavior.
students = {"Alice", "Bob", "Charlie", "David"}
students.remove("Charlie")
print(students)
students.discard("Eve")
print(students)


#15.Given a list numbers_list = [1, 2, 3, 4, 4, 5, 5], convert this list to a set to remove duplicates and print the resulting set.
numbers_list = [1, 2, 3, 4, 4, 5, 5]
remove_duplicates =set(numbers_list)
print(remove_duplicates)

#16.Given a string text = "hello", convert this string to a set to find the unique characters and print the resulting set.
text = "hello"
unique_chars =set(text)
print(unique_chars)

#17.Create a set called vehicles with values {"car", "bike", "bus", "train"}. Find out how many items are in the set and print the result.
vehicles = {"car", "bike", "bus", "train"}
print(len(vehicles))


#18.Given the set gadgets = {"laptop", "smartphone", "tablet", "smartwatch"}, print the number of items in the set.
gadgets ={"laptop", "smartphone", "tablet", "smartwatch"}
print(len(gadgets))



# # user_word = input("enter a word : ")
# # if user_word.lower()startswith("a")
# #        print("it starts with a")
# # else:
# #      print("It does not start with a")


# # sentence = input("Enter a sentence: ")
# # if sentence.islower() :
# #     print("it is in lowercase")
# # else:
# #     print("Not  everything is in lowercase")


# score = input("Enter your score: ")
# if 0 <= score <= 29:
#     print("F")
# elif 30 <= score <= 59:
#     print("C")
# else:
#     print("A")



# has_umbrella = True
# has_raincoat = False

# if has_umbrella or has_raincoat:
# print("You are ptotected from the rain")

# if has_umbrella and has_raincoat:
#   print("You have Double protection")

# else:
#     print("You are not protected")

    
    
     
# mode = input("Enter mode of supplies").strip().lower()
# if mode  == "Manual"
#     print("Manual mode Activated")
# elif mode == "Automatic"
#       print("Automatic mode activated ")
  
