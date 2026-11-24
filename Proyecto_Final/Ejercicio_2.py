# 2. Categorización de ventas con montos acumulados:
# Clasifica N ventas en tres rangos (<= $300, $301 a $800, > $800),
# mostrando la cantidad, el subtotal por categoría y el total general.

n = int(input("Cuantas ventas vas a registrar?: "))

# Contadores y acumuladores para cada rango
cant1 = 0
monto1 = 0
cant2 = 0
monto2 = 0
cant3 = 0
monto3 = 0

for i in range(1, n + 1):
    venta = float(input("Monto de la venta " + str(i) + ": "))
    
    # Clasificar la venta segun su monto
    if venta <= 300:
        cant1 = cant1 + 1
        monto1 = monto1 + venta
    elif venta <= 800:
        cant2 = cant2 + 1
        monto2 = monto2 + venta
    else:
        cant3 = cant3 + 1
        monto3 = monto3 + venta

total_general = monto1 + monto2 + monto3

print("Ventas <= 300:", cant1, "Subtotal:", monto1)
print("Ventas entre 301 y 800:", cant2, "Subtotal:", monto2)
print("Ventas > 800:", cant3, "Subtotal:", monto3)
print("Total general:", total_general)