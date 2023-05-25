def print_operation_table(operation, i, num_columns=6):
    
    stroka = list(map(operation,list(range(1,num_columns+1)),[i]*num_columns))
    print(*stroka, sep=" ")
    return

num_columns = int(input("Введите число столбцов: "))
num_rows = int(input("Введите число строк: "))

for i in range(1,num_rows+1):
    print_operation_table(lambda x, y: x * y,i,num_columns)