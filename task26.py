def exponentiation(A,B,res):
    if B==0:
       return res
    return exponentiation(A,B-1,A*res)
    
A = int(input("Введите основание А: "))
B = int(input("Введите показатель степени В: "))
print(exponentiation(A,B,1))