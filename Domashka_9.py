import random


def binary_search(nums: list, search_item):
    first_index = 0
    last_index = len(nums) - 1
    search_count = 0

    while first_index <= last_index:
        middle_index = (first_index + last_index) // 2
        if nums[middle_index] == search_item:
            search_count += 1
            print(f"Found {search_item} on index {middle_index} in {search_count} attempts")
            return
        else:
            if search_item < nums[middle_index]:
                search_count += 1
                last_index = middle_index - 1
            else:
                search_count += 1
                first_index = middle_index + 1
    return -1


def generate_random_list(length, min_int, max_int):
    return [random.randint(min_int, max_int) for _ in range(length)]


def bubble_sort(nums: list):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swapped = True
    return nums


while True:
    try:
        len_list = int(input("Enter len of list: "))
        min_int_list = int(input("Enter min int in list: "))
        max_int_list = int(input("Enter max int in list: "))
        search_int = int(input("Enter int to find: "))
        random_list = list(set(generate_random_list(len_list, min_int_list, max_int_list)))
        print(bubble_sort(random_list))
        result = binary_search(bubble_sort(random_list), search_int)
        if result == -1:
            print("Not found")
    except ValueError:
        print("Enter int!")
