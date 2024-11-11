import random
numbers = [random.randint(-50, 50) for _ in range(25)]
print("Початковий список:", numbers)
A1 = []
A2 = []
for i in numbers:
    if i > 0:
        A1.append(i)
    elif i < 0:
        A2.append(i)

print("Список додатних елементів:", A1)
print("Список від'ємних елементів:", A2)
