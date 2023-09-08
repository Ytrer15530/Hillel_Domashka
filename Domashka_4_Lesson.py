user_string = input("Enter string: ")
letters = 0
numbers = 0

for i in user_string:
    if i.isalpha():
        letters += 1
    elif i.isnumeric():
        numbers += 1
print(f"Letters in string -> {letters}, numbers in string -> {numbers}")


