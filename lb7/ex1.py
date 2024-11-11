<<<<<<< HEAD:ex1.py
text = input("Введіть текст: ")
count = text.count('Х')
count+=text.count('x')
if count > 4:
    print("Рядок містить більше ніж чотири літери 'X'.")
else:
    print("Рядок не містить більше ніж чотири літери 'X'.")
=======
import random

n = int(input("Введіть кількість чисел в масиві: ")) 
list_x = [random.randint(0, 50) for _ in range(n)]
list_y = [random.randint(0, 50) for _ in range(n)]

list = []
for x, y in zip(list_x, list_y):
    list.append(x)
    list.append(y)

print("Список X:", list_x)
print("Список Y:", list_y)
print("Поєднаний список:", list)
>>>>>>> e331ca61a8bf39ae182252c02a070a7752bbef74:lb7/ex1.py
