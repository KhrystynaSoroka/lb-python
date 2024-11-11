file1=open("file1.txt","r")
file3=open("file3.txt","w")
symbol1 = input("Введіть перший символ: ")
symbol2 = input("Введіть другий символ: ")
for i in file1:
        if symbol1 in i and symbol2 in i:
            file3.write(i)
file1.close()
file3.close()