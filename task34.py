
def kol_gl(slovo):
    return len(list(filter(lambda x: x in list('АаИиОоЮюУуЯяЕеЁёЫы'),list(slovo))))
   

fraza = str(input("Введите фразу:" )).split()

kol_glasnikh = list(map(kol_gl,fraza))
n = kol_glasnikh[0]
if len(list(filter(lambda x: x == n,kol_glasnikh))) == len(kol_glasnikh):
    print("Парам пам-пам")
else:
    print("Пам парам")


