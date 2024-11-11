text = input("Введіть речення: ")
words = text.split()
average_length = sum(len(i) for i in words) / len(words)
longer = [i for i in words if len(i) > average_length]
print("Середня кількість літер: ",average_length)
print("Слова, кількість літер в яких більше за середню:")
for i in longer:
    print(i)
