while True:
    try:
        day_choice = int(input("Enter number from 1 to 7 or 0 to quit: "))
        match day_choice:
            case 1:
                print("Monday")
            case 2:
                print("Tuesday")
            case 3:
                print("Wednesday")
            case 4:
                print("Thursday")
            case 5:
                print("Friday")
            case 6:
                print("Saturday")
            case 7:
                print("Sunday")
            case 0:
                quit()
            case _:
                print("Only numbers between 1 and 7")
    except ValueError:
        print("Enter integer!")

