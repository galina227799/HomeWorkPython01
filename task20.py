dic=[{1:"A, E, I, O, U, L, N, S, T, R, А, В, Е, И, Н, О, Р, С, Т"},{2:"D, G, Д, К, Л, М, П, У"},
     {3:"B, C, M, P, Б, Г, Ё, Ь, Я "}, {4: "F, H, V, W, Y, Й, Ы"}, {5: "K,Ж, З, Х, Ц, Ч"},
     {8:"J, X, Ш, Э, Ю"}, {10:"Q, Z, Ф, Щ, Ъ"}]
word = input("Введите слово: ")
summa = 0;
for bukva in word:
     for j in dic:
         for k in j.values():
 
             if k.count(bukva.upper())>0:
                 for key in j.keys():
                     summa += key
print(summa)