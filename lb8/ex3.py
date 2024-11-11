text = input("Введіть текстовий рядок: ")
words = text.split()
max_count = 0
words_max = []
words=text.split()
for i in words:
    count_r = i.lower().count('r')
    if count_r > max_count:
        max_count = count_r
        words_max = [i]  
    elif count_r == max_count:
        words_max.append(i)
print("Слова, що містять максимальну кількість літер 'R':")
for i in words_max:
    print(i)
