import random

random_list = []
sum_neg = 0
negative_list = []
even_sum = 0
odd_sum = 0
indexes_mult_3 = 1
min_max_mult = 1

for i in range(10):
    random_number = random.randint(-10, 10)
    random_list.append(random_number)
print(f"Random list -> {random_list}")

for i in random_list:
    if i < 0:
        negative_list.append(i)
# print(negative_list)

for i in negative_list:
    sum_neg += i
print(f"Сумма негативных чисел равна -> {sum_neg}")

for i in random_list:
    if i % 2 == 0:
        even_sum += i
        # print(i, end=" ")
print(f"Сумма парных чисел равна -> {even_sum}")

for i in random_list:
    if i % 2 != 0:
        odd_sum += i
        # print(i, end=" ")
print(f"Сумма непарных чисел равна -> {odd_sum}")

for i in random_list[::3]:
    indexes_mult_3 *= i
    # print(i, end=" ")
print(f"Произведение индексов кратным 3 -> {indexes_mult_3} ")


min_list = random_list.index(min(random_list))
max_list = random_list.index(max(random_list))

if min_list > max_list:
    min_list, max_list = max_list, min_list

for i in random_list[min_list+1: max_list]:
    min_max_mult *= i
print(f"Произведение чисел между макс и мин числом -> {min_max_mult}")
