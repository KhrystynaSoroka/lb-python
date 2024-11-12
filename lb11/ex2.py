def half(numbers):
    mid = (len(numbers) + 1) // 2
    half1 = numbers[:mid]
    half2 = numbers[mid:]
    num_half1 = 0
    num_half2 = 0
    for i in half1:
        if i>0:
            num_half1+=1
    for i in half2:
        if i>0:
            num_half2+=1
    if num_half1 > num_half2:
        print("Більшість додатних елементів знаходяться в першій половині. Їх кількість становить:", num_half1)
    elif num_half2 > num_half1:
        print("Більшість додатних елементів знаходяться в другій половині. Їх кількість становить:", num_half2)
    else:
        print("Кількість додатних елементів однакова в обох половинах. Їх кількість становить:", num_half2)

numbers = [90,-67, 456, -8, 56, 533, 12, -6, -9, 80, 67, 54, 888, -45, 2234, -236, 7, 12, 987, -56]
half(numbers)
