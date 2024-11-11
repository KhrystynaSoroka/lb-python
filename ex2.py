file2 = open("file2.txt", "r")
sum = 0
for i in file2:
    parts = i.split()
    for j in parts:
            num = float(j)
            if num.is_integer():
                sum += int(num)
file2.close()
print("Сума цілих чисел у файлі:", sum)
