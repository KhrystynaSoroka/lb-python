info = "Мене звати Христина. Мені 19 років. Народилася у Львові. Я навчаюся на 4 курсі комп'ютерної спеціальності.  У вільний час мені подобається читати"
print(f"Кількість символів 'а' у тексті: {info.count("а")}")

sentences = info.split(". ")
for sentence in sentences:
    print(sentence.strip()) 
