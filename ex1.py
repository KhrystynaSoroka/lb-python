text1 = input("Введіть перший рядок: ")
text2 = input("Введіть другий рядок: ")
vowels = set("aeiouAEIOU")

S1 = set()
S2 = set()
for i in text1:
    if i in vowels:
        S1.add(i)

for i in text2:
    if i in vowels:
        S2.add(i)        

print("Голосні літери в першому рядку (S1): ", S1)
print("Голосні літери в другому рядку (S2): ", S2)
print("Різниця S2 - S1:", S2 - S1)
print("Різниця S1 - S2:", S1 - S2)