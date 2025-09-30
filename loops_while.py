
# num = int(input('Enter a number: '))

# if num < 6:
#     print("Number is not up to 6. Please try again.")
#     num = int(input('Enter a number: '))


# password = input('Enter password: ')
# cpassword = input('Confirm your password: ')


# while password != cpassword:
#     print('Passwords do not match!')
    
#     password = input('Enter password: ')
#     cpassword = input('Confirm your password: ')


# i = 0
# while i < 3:
#     user_input = input('Enter something here: ')
#     print(user_input * 3)
    
#     i += 1


# i = 6

# while i < 12:
#     print("Hello world")
    
#     i += 1



list_of_footballers = ["Messi", "Haaland", "Lewandowski", "Yamal", "Ronaldo"]


# i = 0
# while i < 4:
#     print(list_of_footballers[i])
#     i += 1
    
    

# i = 0

# while i < len(list_of_footballers):
#     print(list_of_footballers[0])    

#     i += 1



# i = 0
# # list_of_names = []
# total = 0
# while i < 2:
#     name = input('Enter name: ')
#     # list_of_names.append(name)
    
#     i += 1
    

# print(name)
# Write a program that accepts numbers 8 times and then displays the sum of all the numbers.


# i = 0

# total = 0

# while i < 5:
#     num = float(input(f'Enter num {i + 1}: '))
#     total += num
#     i += 1
    
#     print(f"Total right now is: {total}")



# Write a program that keeps asking the user to enter a number they want to deduct for 10 times... Then keep deducting that number from the value of a variable called initial = 2000

initial = 2000

# Loop 10 times
for i in range(10):
    num = int(input(f"Enter number to deduct ({i+1}/10): "))
    initial -= num
    print(f"After deduction {i+1}, remaining = {initial}")

print("\nFinal value after 10 deductions:", initial)


# while True:
#     username= input('Enter your username: ')
    
#     if not len(username) < 8:
#         break
        
#     else:
#         print('Username is too short.')
        
        




# from random import randint

# computer_guess = randint(1, 20)

# for i in range(5):
#     userguess = int(input('Enter your guess: '))
#     print(f"Hint: {computer_guess}")
#     if userguess == computer_guess:
#         print('Correct guess')
#         break
    
#     else:
#         print("Incorrect guess")    
#         continue


# mystring = "Hippoppotamus"

# for i in range(9):
#     print(mystring[i])


# animal = "Hippoppotamus"

# for ch in animal:
    

# cars = ["BMW", "Volvo", "Rolls Royce", "Toyota"]

# # for i in range(len(cars)):
# #     print(cars[i])


# for car in cars:
#     print(car)


# for i in range(10):
#     pass




# even_numbers = []

# for i in range(1, 301):
#     if i % 2 == 0:
#         even_numbers.append(i)
        

# print(f"My even numbers are: {even_numbers}")


# [what_to_append loop]
# [what_to_append condition loop]


# numbers = ["Tobi" * 2 for i in range(15)]
# print(numbers)


# numbers = []

# for i in range(15):
#     numbers.append("Tobi" * 2)

# print(numbers)



# numbers = ["Tobi" * 2 for i in range(15) if i not in [2, 4, 7, 3]]


# scores = [34, 65, 4, 56, 43, 566, 34, 3,23, 65, 87, 67, 878]

# scores_description = ["High" if score > 50 else "Low" for score in scores]

# print(scores)

# print(scores_description)


# even_numbers = [i for i in range(1, 301) if i % 2 == 0]

# # scores_description = []

# for score in scores:
#     if score >= 50:
#         scores_description.append("High")
#     else:
#         scores_description.append("Low")






# x = [4, 5, 34, 65, 34, 23, 54, 3, 45, 23, 56]

# y = [number > 20 for number in x]


# print(all(y))



# word = input('Enter a word: ')

# flag = False

# for letter in word:
#     if letter in 'ABCDEGHIJKLMNOPQRSTUVWXYZ':
#         flag = True
#         break


# upper_case_check = [ch in 'ABCDEGHIJKLMNOPQRSTUVWXYZ' for ch in word]
# upper_case_check = [ch in 'ABCDEGHIJKLMNOPQRSTUVWXYZ' for ch in word]

# print(any(upper_case_check))












