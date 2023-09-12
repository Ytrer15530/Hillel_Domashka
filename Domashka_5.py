import random

random_list = []
sum_neg = 0
negative_list = []
even_sum = 0

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

