num = [56, 78, 32, 45, 17, 20]
print("Початковий список:", num)

num.insert(1, -5)
print("Список після додавання -5:", num)

min_num = min(num)
max_num = max(num)
print("Мінімальний елемент:", min_num)
print("Максимальний елемент:", max_num)

new_num = [1, 2, 3]
num.insert(3, new_num)
print("Список після додавання [1, 2, 3]:", num)

name = ["Сорока", "Христина"]
num.append(name)
print("Список після додавання прізвища та імені:", num)

count = len(num)
print("Кількість елементів у списку:", count)
