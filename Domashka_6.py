import random

# random_list = [random.randint(0, 10) for i in range(10)]
# print(random_list)
# set_list = set(random_list)
# print(set_list)
#
#
# list_1 = set([random.randint(0, 10) for k in range(10)])
# list_2 = set([random.randint(0, 10) for j in range(10)])
# count = 0
# for i in list_1:
#     if i in list_2:
#         count += 1
# print(count)
# print(list_1)
# print(list_2)
#
#
# words_list = []
# words_count = 0
# text ="""Словом вважається послідовність непробільних символів, що йдуть поспіль,
# слова розділені одним або більшим числом пробілів або символами кінця рядка."""
#
# for words in text.split():
#     if words not in words_list:
#         words_list.append(words)
#         words_count += 1
# print(words_list)
# print(words_count)

country_city = {
    "Ukraine": ["Kyiv", "Lviv", "Dnipro"],
    "USA": ["Los Angeles", "Las Vegas"]
}

while True:
    City_Name = input("Enter city: ").lower()
    found = False

    for country, city in country_city.items():
        for temp_city in city:
            if City_Name == temp_city.lower():
                print(f" Этот город находится в -> {country}")
                found = True
    if not found:
        print("City not found!")

# print(country_city.items())
