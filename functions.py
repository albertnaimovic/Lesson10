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


# def string_lenght(my_string):
#     letters_list = []
#     my_string = my_string.replace(" ", "")
#     for char in my_string:
#         letters_list.extend(char)
#     return len(letters_list)


# def count_letters(my_string: str):
#     return len(my_string.replace(" ", ""))

# print(string_lenght("labas       as       Albertas"))
# print(count_letters("labas       as       Albertas"))

# def add_two_numbers(a: int, b: int) -> int:
#     return a + b
# def number_square(a: int) -> int:
#     return a ** 2
# def make_a_string(my_text: str, my_num: int) -> str:
#     number = number_square(my_num)
#     return my_text+str(number)
# print(make_a_string("zodis", 5))


# 1. 
# def create_list(x: int) -> list:
#     return [x for x in range(x+1)] 

# def list_extend(x: int) -> list:
#     a_list = [10, 10, 10]
#     a_list.extend(create_list(x))
#     return a_list

# def sum_list(x: list) -> int:
#     return sum(list_extend(x))

# def count_words(my_text: str) -> int:
#     my_list = my_text.split(" ")
#     words_lenght = len([word for word in my_list])
#     return words_lenght

# def union_of_functions(x:int, my_text: str):
#     return f"Sum of the list: {sum_list(x)} and the lenght of string {count_words(my_text)}"

# print(union_of_functions(5, "vienas du trys keturi"))


# from typing import List

# simbol = input("Please enter words with spec simbol: ")

# def find_word(in_text: str) -> List[str]:
#     unique_chars: List[str] = ["!","@","#","$","%","^","&","*","_","+","-"]
#     splited_words: List[str] = in_text.split(" ")
#     unique_words: List[str] = [word for word in splited_words if any(simb in word for simb in unique_chars)]
#     return unique_words

# print(find_word(simbol))

# Task nr.1: Create a mini program that takes 10 random numbers in one input ("1,2,5 76,89 ...etc") Write functions to: 
# calculate their sum, multiplication of highest and lowest numbersand and the function which makes a new string where numbers are positioned from highest to lowest.

# random_nums: str = "3,23,65,234,646,22,9,8,25,5"

# list_of_strings: list = random_nums.split(",")
# list_of_ints: list = [int(x) for x in list_of_strings]

# def random_num_sum(numbers: list) -> int:
#     return sum(numbers)

# def lowest_and_highest_multiplication(list_of_numbers: list) -> int:
#     return max(list_of_numbers) * min(list_of_numbers)

# def num_order_desc(list_of_numbers: list) -> str:
#     list_of_numbers.sort(reverse=True)
#     sorted_nums_string: str = " ".join([str(x) for x in list_of_numbers])
#     return sorted_nums_string

# print(f"Sum of numbers: {random_num_sum(list_of_ints)}")
# print(f"Multiplication of highest and lowest numbers: {lowest_and_highest_multiplication(list_of_ints)}")
# print(f"String of numbers in descending order: {num_order_desc(list_of_ints)}")



# Task nr.2:
# Create a program , which takes 3 different sentences. The input should have all error checking in mind. 
# The program then should create a dictionary of whitch key values corresponding to words `long` (more than 9 letters in a words) `medium`(7 letters)`short` (5 words).
# Then the program should create a new sentences (if 3 provided, 3 new sentences should be returned) with following rules attached:
# All sentences should have same (or less) words amount as entered one;
# The most frequent letter from the sentence (from input) should be dominated in a new sentence as well.

# The program should return new sentences with statitstics of ratio how many words was used from all sections 
# (as for exmpale: long 25%,medium 45%, short 30%)

# three_sentences: str = "A bridge is a structure built to span a physical obstacle (such as a body of water, valley, road, or railway) without blocking the way underneath. It is constructed for the purpose of providing passage over the obstacle, which is usually something that is otherwise difficult or impossible to cross. There are many different designs of bridges, each serving a particular purpose and applicable to different situations."
# list_of_strings: list = three_sentences.split(" ")
# cleaned_list: list =  [x.replace(".", "").replace(",", "").replace("(", "").replace(")", "").replace("?", "").replace("!", "") for x in list_of_strings]

# def create_dict_with_lenghts(cleaned_list: str) -> dict:
#     long: list = [x for x in cleaned_list if len(x) > 9]
#     medium: list = [x for x in cleaned_list if len(x) <= 9 and len(x) >= 5]
#     short: list = [x for x in cleaned_list if len(x) < 5]
#     long_percent: float = len(long) * 100 / len(cleaned_list)
#     medium_percent: float = len(medium) * 100 / len(cleaned_list)
#     short_percent: float = len(short) * 100 / len(cleaned_list)
#     dict_with_lenghts: dict = {"long": f"{round(long_percent, 2)}%", "medium": f"{round(medium_percent, 2)}%", "short": f"{round(short_percent, 2)}%"}
#     return dict_with_lenghts

# print(create_dict_with_lenghts(cleaned_list))



# User enters two names separated by comma : for example :('Mindaugas PiktasDestytojas, Mindaugas Juokauja') 
# Create a function that would swipe surnames and will prduxe new name surname and 
# another function funtion that will swap names.

names_surnames: str = "Albert Naimovic, Karina Krysko"


def swap_surnames(names_surnames: list) -> list:
    list_of_names_surnames = names_surnames.replace(",", "").split(" ")
    my_order = [1, 4, 2, 1]
    list_of_names_surnames = [list_of_names_surnames[i] for i in my_order]
    return list_of_names_surnames

    
    
    
print(swap_surnames(names_surnames=names_surnames))
