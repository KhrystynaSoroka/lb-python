import random
name = input("Введіть ім'я: ")
surname = input("Введіть прізвище: ")
n = len(name)  
m = len(surname)  
matrix = [[random.randint(0, 20) for _ in range(n)] for _ in range(m)]
print("Початкова матриця:")
for row in matrix:
    print(row)

max_value = min_value = matrix[0][0]
max_index = min_index = 0
for i in range(m):
    for j in range(n):
        if matrix[i][j] > max_value:
            max_value = matrix[i][j]
            max_index = i
        if matrix[i][j] < min_value:
            min_value = matrix[i][j]
            min_index = i

matrix[max_index], matrix[min_index] = matrix[min_index], matrix[max_index]
print("\nМатриця після заміни рядків:")
for row in matrix:
    print(row)
file4 = open("file4.txt", 'w') 
for row in matrix:
    file4.write(' '.join(map(str, row)) + '\n')
file4.close() 
