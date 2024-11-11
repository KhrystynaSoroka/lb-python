text = input("Введіть текстовий рядок: ")
words = []
for i in text.split():
    if 'а' not in i.lower():  
        words.append(i)

numbers = []
for word in words:
    set1 = set()  
    for char in word:
        if char.isdigit(): 
            set1.add(char) 
    if set1:  
        numbers.append(set1)

if numbers:
    intersection = set.intersection(*numbers)
else:
    intersection = set()

print("Слова, які не містять літери 'а':", words)
print("Перетин всіх множин цифр:", intersection)
