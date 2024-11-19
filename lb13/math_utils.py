def add(a,b):
    return a+b
def minus(a,b):
    return a-b
def mult(a,b):
    return a*b
def division(a,b):
    return a/b
def number_to_text(num):
    match num:
        case 1: return "Один"
        case 2: return "Два"
        case 3: return "Три"
        case 4: return "Чотири"
        case 5: return "П'ять"
        case 6: return "Шість"
        case 7: return "Сім"
        case 8: return "Вісім"
        case 9: return "Дев'ять"
        case  10: return "Десять"
        