# Problema 6: El mayor de dos números
# Compara dos números y regresa el más grande sin max().
# --------------------------------------------------
def mayor_de_dos(a, b):
    # si a es mayor regresa a, si no regresa b
    if a > b:
        return a
    else:
        return b

# Pruebas
print(mayor_de_dos(30, 15))  
print(mayor_de_dos(15, -7)) 
print(mayor_de_dos(100, 23))    
