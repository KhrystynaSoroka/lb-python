import random

n = len(input("Введіть ім'я: "))    
m = len(input("Введіть прізвище: ")) 
matrix = [[random.randint(0, 20) for _ in range(n)] for _ in range(m)]
print("Початкова матриця:")
for i in matrix:
    print(i)

max = min = matrix[0][0]
max_index = min_index = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] > max:
            max = matrix[i][j]
            max_index = i
        if matrix[i][j] < min:
            min = matrix[i][j]
            min_index = i

matrix[max_index], matrix[min_index] = matrix[min_index], matrix[max_index]
print("\nМатриця після заміни рядків:")
for i in matrix:
    print(i)