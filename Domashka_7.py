import random


def mult_list(numbers: list):
    numbers_mult = 1
    for num in numbers:
        numbers_mult *= num
    return numbers_mult


random_numbers_list = [random.randint(1, 10) for i in range(10)]
print(random_numbers_list)
print(f"Произведение списка -> {mult_list(random_numbers_list)}")

