num=[1,2,3,4,5,6,7,8,9,10]
for i in num:
    if i % 2 == 0:  
        result = i ** 2
        print(f"Квадрат числа {i} дорівнює {result}")
    else:  
        result = i ** 3
        print(f"Куб числа {i} дорівнює {result}")
