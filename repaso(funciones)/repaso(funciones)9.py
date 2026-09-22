# Problema 9: Obtener el signo de un número
# Clasifica un número en Positivo, Negativo o Cero.
# --------------------------------------------------
def obtener_signo(numero):
    # revisamos si es mayor, menor o igual a cero
    if numero > 0:
        return "Positivo"
    elif numero < 0:
        return "Negativo"
    else:
        return "Cero"

# Pruebas
print(obtener_signo(20)) 
print(obtener_signo(-12)) 
print(obtener_signo(0))   
