s = int(input("Введите количество сделанных журавликов: "))
if s%2 != 0 or s<6 or s%6 != 0:
    print("Не верные данные")
else:
    print("Петя:",s//6, "Катя:",s//6*4, "Сережа:",s//6)