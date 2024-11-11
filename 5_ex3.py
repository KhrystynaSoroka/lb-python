N = int(input("Введіть значення N: "))
a, b = 0, 1
print(a)
while b % N != 0:
    print(b)
    a, b = b, a + b
print(b)