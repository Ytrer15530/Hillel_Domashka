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


prime_nums = []


def find_prime_numbers(numbers: list):
    for num in numbers:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
                else:
                    prime_nums.append(num)
                    break
    return prime_nums


def len_prime_list(prime_list: list):
    return len(prime_list)


def remove_number(numbers, number_to_remove):
    remove_count = 0
    for num in numbers:
        if num != number_to_remove:
            continue
        else:
            remove_count += 1
    return remove_count


def get_same_numbers_in_list(numbers_1: list, numbers_2: list):
    same_list = []
    for i in set(numbers_1):
        if i in numbers_2:
            same_list.append(i)
    return same_list


random_numbers_list = [random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER) for i in range(10)]
random_numbers_list_2 = [random.randint(MIN_RANDOM_NUMBER, MAX_RANDOM_NUMBER) for j in range(10)]
print(random_numbers_list)
print(random_numbers_list_2)
print(f"Произведение списка -> {mult_list(random_numbers_list)}")
print(f"Минимум в списке -> {find_minimum(random_numbers_list)}")
# print(find_prime_numbers(random_numbers_list))
print(f"Количество простых чисел в списке -> {len_prime_list(find_prime_numbers(random_numbers_list))}")
remove_int = int(input("Enter number to remove: "))
print(f"Количество удаленных чисел -> {remove_number(random_numbers_list, remove_int)}")
print(get_same_numbers_in_list(random_numbers_list, random_numbers_list_2))

