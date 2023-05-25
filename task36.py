def sootv(slovo):
    slovo = list(slovo.split("="))
    return (slovo[0],slovo[1])
   

#fraza = str(input("Введите соответствия:" )).split()
fraza = "house=дом car=машина men=человек tree=дерево".split()
tp = tuple(map(sootv,fraza))
print(tp)

