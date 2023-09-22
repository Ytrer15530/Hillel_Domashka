def mult_rec(number, degree):
    if degree <= 1:
        return number
    return number * mult_rec(number, degree-1)


print(mult_rec(3, 3))

# 3 * mult_rec(3, 2) -> 9 * 3 -> 27
# 3 * mult_rec(3, 1) -> 3 * 3 -> 9
# 3

star_int = int(input("Enter number of stars: "))


def star_line(n):
    if n <= 0:
        return
    else:
        print("*", end="")
        star_line(n-1)


star_line(star_int)

# n = 3
# n3 > 0 -> *
# n2 > 0 -> **
# n1 > 0 -> ***
# n 0 = 0 end


int_a = int(input("\nEnter number for a: "))
int_b = int(input("Enter number for b: "))


def sum_between(a, b):
    if a > b:
        return 0
    return a + sum_between(a+1, b)


print(f"Сумма чисел между {int_a} и {int_b} -> {sum_between(int_a, int_b)}")

# a=1 b =3
# 1 < 3 -> a = 1
# 2 < 3 -> a = 2
# 3 !> 3 -> a = 3
# 4 > 3 -> 0
# 0 + 3 -> 3
# 3 + 2 -> 5
# 5 + 1 -> 6
