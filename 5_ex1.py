a = float(input("Введіть значення a: "))
b = float(input("Введіть значення b: "))
N = int(input("Введіть кількість членів послідовності N: "))
sum = 0
for i in range(N):
    g = (a**2 + b**2) / (a**2 + b**2 + 4)  
    sum += g  
print(f"Сума перших {N} членів послідовності: {sum}")
