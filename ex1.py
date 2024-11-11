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