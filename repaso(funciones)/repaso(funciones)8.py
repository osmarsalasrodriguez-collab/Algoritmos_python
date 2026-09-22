# Problema 8: Calcular área de un triángulo
# Valida que base y altura sean mayores a 0 antes de calcular.
# --------------------------------------------------
def area_triangulo(base, altura):
    # si alguno es 0 o negativo regresa 0
    if base <= 0 or altura <= 0:
        return 0
    # formula del area
    return (base * altura) / 2

# Pruebas
print(area_triangulo(10, 5)) 
print(area_triangulo(7, 4))  
print(area_triangulo(-2, 5)) 