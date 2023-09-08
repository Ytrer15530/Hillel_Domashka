# user_string = input("Enter string: ")
# letters = 0
# numbers = 0
#
# for i in user_string:
#     if i.isalpha():
#         letters += 1
#     elif i.isnumeric():
#         numbers += 1
# print(f"Letters in string -> {letters}, numbers in string -> {numbers}")


# TASK 2

string_input = input("Enter string: ")
symbol_search = input("What symbol to search?: ")
symbol_count = 0

for i in string_input:
    if i == symbol_search:
        symbol_count += 1
print(f"In string {symbol_count} {symbol_search}'s")

# Task 3

string_input = input("Enter string: ").lower()
what_word = input("What word you want to change?: ").lower()
what_to = input("On what word you want to change?: ").lower()
print(f"Your string is -> {string_input.replace(what_word, what_to).title()}")



