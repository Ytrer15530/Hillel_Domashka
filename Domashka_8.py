def mult_rec(number, degree):
    if degree <= 1:
        return number
    return number * mult_rec(number, degree-1)


print(mult_rec(3, 3))

# 3 * mult_rec(3, 2) -> 9 * 3 -> 27
# 3 * mult_rec(3, 1) -> 3 * 3 -> 9
# 3
