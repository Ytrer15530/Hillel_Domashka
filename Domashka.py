# while True:
#     try:
#         day_choice = int(input("Enter number from 1 to 7 or 0 to quit: "))
#         match day_choice:
#             case 1:
#                 print("Monday")
#             case 2:
#                 print("Tuesday")
#             case 3:
#                 print("Wednesday")
#             case 4:
#                 print("Thursday")
#             case 5:
#                 print("Friday")
#             case 6:
#                 print("Saturday")
#             case 7:
#                 print("Sunday")
#             case 0:
#                 quit()
#             case _:
#                 print("Only numbers between 1 and 7")
#     except ValueError:
#         print("Enter integer!")

# while True:
#     try:
#         number1 = int(input("Enter first number: "))
#         number2 = int(input("Enter second number: "))
#         if number1 == number2:
#             print("Равные числа")
#         elif number1 < number2:
#             print(f"{number1} -> {number2}")
#         else:
#             print(f"{number2} -> {number1}")
#     except ValueError:
#         print("Enter Integer!")

while True:
    try:
        operator_choice = input("Choose +, - , * or / : ")
        first_number = int(input("Enter first number: "))
        second_number = int(input("Enter second number: "))
        match operator_choice:
            case "+":
                print(f"{first_number} + {second_number} = {first_number + second_number}")
            case "-":
                print(f"{first_number} - {second_number} = {first_number - second_number}")
            case "*":
                print(f"{first_number} * {second_number} = {first_number * second_number}")
            case "/":
                print(f"{first_number} / {second_number} = {first_number / second_number}")
            case _:
                print("Enter valid operator")
    except ValueError:
        print(f"Enter number")