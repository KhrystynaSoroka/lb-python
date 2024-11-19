def prime_number(n,d=2):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % d == 0:
        return False
    if d * d > n:
        return True
    else:
        return prime_number(n, d + 1)

n = int(input("Введіть натуральне число--> "))
if n > 1 and prime_number(n):
    print("Число є простим.")
else:
    print("Число не є простим.")
