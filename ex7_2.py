char = input("Введіть символ: ")
punctuation_marks = [',', '.', '!', '?', ':', ';', '-', '(', ')', '[', ']', '{', '}', '"', "'"]
if char in punctuation_marks:
    print("Є розділовим знаком.")
else:
    print("Не є розділовим знаком.")
