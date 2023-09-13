import random
column = []
matrix = []
main_diag = 0
min_diag = 0
max_diag = 0
sec_diag = []
row_input = int(input("Enter number of row: "))
column_input = int(input("Enter number of column: "))
# row_replace_1 = int(input("Enter first row you want to replace: "))
# row_replace_2 = int(input("Enter second row you want to replace: "))
# matrix_copy = None

for i in range(10):
    matrix.append([])
    for j in range(10):
        matrix[i].append(random.randint(10, 99,))

for row in matrix:
    for number in row:
        print(number, end=" ")
    print()

for row in range(len(matrix)):
    main_diag += matrix[row][row]
    column.append(matrix[row][column_input])

for row in range(len(matrix)):
    sec_diag.append(matrix[::-1][row][row])
# print(sec_diag)

for number in sec_diag:
    max_diag = max(sec_diag)
    min_diag = min(sec_diag)

match row_input:
    case 0:
        print(f"Первый ряд -> {matrix[0]}")
    case 1:
        print(f"Второй ряд -> {matrix[1]}")
    case 2:
        print(f"Третий ряд -> {matrix[2]}")
    case 3:
        print(f"Четвертый ряд -> {matrix[3]}")
    case 4:
        print(f"Пятый ряд -> {matrix[4]}")
    case 5:
        print(f"Шестой ряд -> {matrix[5]}")
    case 6:
        print(f"Седьмой ряд -> {matrix[6]}")
    case 7:
        print(f"Восьмой ряд -> {matrix[7]}")
    case 8:
        print(f"Девятый ряд -> {matrix[8]}")
    case 9:
        print(f"Десятый ряд -> {matrix[9]}")


print(f"{column_input + 1} колонка -> {column}")
print(f"Сумма главной диагонали -> {main_diag}")
print(f"Мин Макс побочной диагонали -> {min_diag}, {max_diag}")
