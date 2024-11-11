N = int(input("Введіть значення N: "))
if 2 <= N < 99:
    for i in range(1, N + 1):
        row = [] 
        for j in range(1, N + 1):
            if j % 2 == 0:
                row.append("0")
            else:
                value = i * 100 + j * 10
                row.append(str(value))
        print(" ".join(row))
else:
    print("Значення N повинно бути в діапазоні 2 <= N < 99")
