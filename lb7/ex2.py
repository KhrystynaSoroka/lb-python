<<<<<<< HEAD:ex2.py
text = input("Введіть текстовий рядок: ")
words = text.split()
words_without_a = [word for word in words if 'а' not in word and 'А' not in word]
print("Слова, які не містять літери 'а':")
for word in words_without_a:
    print(word)
=======
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
>>>>>>> e331ca61a8bf39ae182252c02a070a7752bbef74:lb7/ex2.py
