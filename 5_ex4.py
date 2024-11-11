import math

a = float(input("Введіть початкове значення відрізку: "))
b = float(input("Введіть кінцеве значення відрізку: "))
h = float(input("Введіть крок: "))
x = a
print("Табуляція значень функції:")
while x <= b:
    if x == 0:
        print("На 0 ділити не можна")
    else:
        y = (1 / x) + math.sqrt(x + 3) + 6
        print(f"x = {x}, y = {y}")
    x += h
print("Табуляція закінчена.")
