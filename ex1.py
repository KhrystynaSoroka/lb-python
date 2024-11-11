text = input("Введіть текст: ")
count = text.count('Х')
count+=text.count('x')
if count > 4:
    print("Рядок містить більше ніж чотири літери 'X'.")
else:
    print("Рядок не містить більше ніж чотири літери 'X'.")
