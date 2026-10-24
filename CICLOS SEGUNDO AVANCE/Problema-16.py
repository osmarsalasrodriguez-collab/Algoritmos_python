# Problema 16: Un empleado de la tienda "Tiki Taka" realiza N ventas durante el día, se requiere saber cuántas de ellas
# fueron mayores a $1000, cuántas fueron mayores a $500 pero menores o iguales a $1000, y cuántas fueron
# menores o iguales a $500. Además, se requiere saber el monto de lo vendido en cada categoría y de forma global

ventas = int(input("¿Cuántas ventas hiciste hoy?: "))

# Contadores de ventas por categoría
c1 = 0
c2 = 0
c3 = 0

# Acumuladores de dinero
monto1 = 0
monto2 = 0
monto3 = 0

for i in range(ventas):
    monto = float(input("Ingresa el monto de la venta: "))
    
    # Clasificación por rangos de precio
    if monto > 1000:
        c1 = c1 + 1
        monto1 = monto1 + monto
    elif monto > 500:
        c2 = c2 + 1
        monto2 = monto2 + monto
    else:
        c3 = c3 + 1
        monto3 = monto3 + monto

# Sumamos los tres montos parciales para obtener el total global
total = monto1 + monto2 + monto3

print("Ventas mayores a 1000:", c1, " Total:", monto1)
print("Ventas entre 500 y 1000:", c2, " Total:", monto2)
print("Ventas menores o iguales a 500:", c3, " Total:", monto3)
print("Total vendido global:", total)