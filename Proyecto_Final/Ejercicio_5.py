# 5. Inventario y conteo por tipo de producto:
# Clasifica N artículos según su código (1: Electrónica, 2: Ropa, 3: Alimentos)
# y calcula la cantidad y el porcentaje que representa cada categoría.

n = int(input("Cuantos articulos vas a ingresar?: "))
elec = 0
ropa = 0
alim = 0

for i in range(1, n + 1):
    codigo = int(input("Codigo del articulo " + str(i) + " (1-Electronica, 2-Ropa, 3-Alimentos): "))
    
    # Validar que el codigo sea correcto
    while codigo < 1 or codigo > 3:
        print("Error, codigo no valido")
        codigo = int(input("Ingresa nuevamente (1, 2 o 3): "))
        
    # Sumar al contador correspondiente
    if codigo == 1:
        elec = elec + 1
    elif codigo == 2:
        ropa = ropa + 1
    else:
        alim = alim + 1

# Calcular porcentajes
porc_elec = (elec * 100) / n
porc_ropa = (ropa * 100) / n
porc_alim = (alim * 100) / n

print("Electronica:", elec, "-", round(porc_elec, 2), "%")
print("Ropa:", ropa, "-", round(porc_ropa, 2), "%")
print("Alimentos:", alim, "-", round(porc_alim, 2), "%")