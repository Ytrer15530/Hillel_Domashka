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


