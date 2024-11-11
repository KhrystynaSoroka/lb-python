age=int(input("Введіть вік користуача: "))

if age<6:
    print("ще не школяр")
elif 6<=age<=9:
    print("початкова школа")
elif 10<=age<=15:
    print("середня школа")
elif 16<=age<=17:
    print("старша школа")
elif age>17:
    print("вже не школяр")