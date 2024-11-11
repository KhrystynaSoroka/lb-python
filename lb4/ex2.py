a=float(input("Введіть перше число: "))
b=float(input("Введіть друге число: "))
c=float(input("Введіть третє число: "))

if a==b==c:
    print(3)
elif  a == b or a == c or b == c:
    print(2)
else:
    print(0)
