num=[1,45,67,96,35,35,7,69,90,34,72, 41, 18,62]

def quick_sort(num):
    if len(num) <= 1:
        return num
    pivot = num[-1]
    smaller, equal, larger = [], [], []
    for num in num:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)
    return quick_sort(smaller) + equal + quick_sort(larger)

print("Швидке сортування: ", quick_sort(num))

def find_element(num, value):
    if value in num:
        print("Індекс елемента: ", num.index(value))  
    else:
        print("Помилка")
print("Пошук елемента 45: ")
find_element(num, 45)

def five_min(num):
    num2=sorted(num)
    return num2[:5]
print("Пошук перших п’яти мінімальних елементів: ", five_min(num))

def avg(num):
    return sum(num) / len(num)
print("Середнє значення: ", avg(num))

def new_list(num):
    num2 = []
    for i in num:
        if i not in num2:
            num2.append(i)
    return num2
print("Повернення списку, що сформований з початкового списку, але не містить повторів:", new_list(num))

