import random
MAX_RANDOM_NUMBER = 10
MIN_RANDOM_NUMBER = 1


def mult_list(numbers: list):
    numbers_mult = 1
    for num in numbers:
        numbers_mult *= num
    return numbers_mult


def find_minimum(numbers: list):
    min_number = min(numbers)
    return min_number


random_numbers_list = [random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER) for i in range(10)]

print(random_numbers_list)
print(f"Произведение списка -> {mult_list(random_numbers_list)}")

print(f"Минимум в списке -> {find_minimum(random_numbers_list)}")
