text = input("Введіть текстовий рядок: ")
words = text.split()
words_without_a = [word for word in words if 'а' not in word and 'А' not in word]
print("Слова, які не містять літери 'а':")
for word in words_without_a:
    print(word)
