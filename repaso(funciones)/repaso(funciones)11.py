# Problema 11: El mayor de tres números
# Encuentra el número más grande usando operadores logicos (and).
# --------------------------------------------------
def mayor_de_tres(a, b, c):
    # comprobamos cada caso con and
    if a >= b and a >= c:
        #si a es mayor que b y c aparece que a es mayor
        return a
    elif b >= a and b >= c:
        #si b es mayor que a y c aparece es b es mayor
        return b
    else:
        #y si no c es la mayor
        return c

# Pruebas llamando 3 numeros
print(mayor_de_tres(53, 120, 91)) 
print(mayor_de_tres(20, 63, 10)) 
print(mayor_de_tres(5, 5, 5))