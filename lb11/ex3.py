import math

def func(n,x):
    if n==1:
        return math.cos(x)*math.sin(x)
    elif n==2:
        return math.sin(x*x)+math.cos(x)
    else:
        return 1-math.sin(x)
n=int(input("Введіть значення n--> "))
x=float(input("Введіть значення x--> "))
print("Результат--> ", func(n,x))