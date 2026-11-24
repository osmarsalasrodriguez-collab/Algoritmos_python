# 12. Cálculo de comisión decreciente para vendedores:
# Calcula la comisión de N ventas (10% si >$1500, 5% entre $500-$1500, 0% si <$500),
# sumando el total de comisiones e identificando la venta más alta.

n = int(input("Numero de ventas: "))
total_comisiones = 0
venta_mayor = 0

for i in range(1, n + 1):
    monto = float(input("Monto de la venta " + str(i) + ": "))
    
    # Guardar la venta si es la mayor hasta ahora
    if monto > venta_mayor:
        venta_mayor = monto
        
    # Calcular porcentaje de comision
    if monto > 1500:
        comision = monto * 0.10
    elif monto >= 500:
        comision = monto * 0.05
    else:
        comision = 0
        
    total_comisiones = total_comisiones + comision

print("Total de comisiones:", round(total_comisiones, 2))
print("La venta mas alta fue:", venta_mayor)