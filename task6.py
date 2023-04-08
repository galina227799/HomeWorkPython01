n = input("Введите номер билета: ")
if len(n)!=6: print("Номер должен быть шестизначным!")
else:
    if int(n[0])+int(n[1])+int(n[2]) == int(n[3])+int(n[4])+int(n[5]): print("Билет счастливый")
    else: print("Билет не счастливый")