a = input("Введіть дужку: ")

if a == '(' or a == ')':
    print("Кругла дужка")
elif a == '[' or a == ']':
    print("Квадратна дужка")
elif a == '{' or a == '}':
    print("Фігурна дужка")
else:
    print("Це не дужка")
