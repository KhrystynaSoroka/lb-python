file1=open("file1.txt","r")
str=input("Введіть послідовність символів: ")
line_number = 1
for i in file1:
    if str in i:  
        print(f"Рядок {line_number}: {i.strip()}")  
    line_number += 1
file1.close()