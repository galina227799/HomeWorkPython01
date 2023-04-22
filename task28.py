def summa(A,B):
    if B==0:
       return A
    return summa(A+1,B-1)
    
A = int(input("Введите число А: "))
B = int(input("Введите число В: "))
print(summa(A,B))