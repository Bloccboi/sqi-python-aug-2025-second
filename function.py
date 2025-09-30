# def multiply_two_nums(first_num,second_num):
#     print(f"The multiplaction of {first_num}and {second_num} is {first_num*second_num}")


# multiply_two_nums(3,9)

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    

print(is_even(7))

def starts_with_a(word):
    if len(word) == 0:
        return False
    return word[0].lower() == 'a'
print(starts_with_a("Ayomide"))
print(starts_with_a("John"))