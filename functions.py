# def add_two_numbers(a, b):
#     print(a + b)

# add_two_numbers(6, 6)
# add_two_numbers(1, 3)
# add_two_numbers(8, 7)


# def say_labas():
#     print("Labas")

# say_labas()


# def add_two_numbers(a, b):
#     return a + b

# my_sum = add_two_numbers(1, 3)
# print(my_sum)

# 1. Create a function that takes string as parameter and returns number of letters from that string.


def string_lenght(my_string):
    letters_list = []
    for char in my_string:
        letters_list.extend(char)
    return len(letters_list)
    
print(string_lenght("labas"))
