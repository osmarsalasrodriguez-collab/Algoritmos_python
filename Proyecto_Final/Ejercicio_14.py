# 14. Actualización de precios por inflación:
# Aplica aumentos escalonados a N productos (5% si <$100, 8% hasta $500,
# 12% si >$500), mostrando la comparativa y la diferencia total del ajuste.

n = int(input("Cuantos productos son?: "))
suma_anteriores = 0
suma_nuevos = 0

for i in range(1, n + 1):
    precio = float(input("Precio del producto " + str(i) + ": "))
    
    # Aplicar el aumento segun el precio original
    if precio < 100:
        nuevo_precio = precio * 1.05
    elif precio <= 500:
        nuevo_precio = precio * 1.08
    else:
        nuevo_precio = precio * 1.12
        
    print("Producto", i, "- Antes:", precio, "- Nuevo:", round(nuevo_precio, 2))
    
    suma_anteriores = suma_anteriores + precio
    suma_nuevos = suma_nuevos + nuevo_precio

# Calcular cuanto subio en total
diferencia = suma_nuevos - suma_anteriores
print("Diferencia total del ajuste:", round(diferencia, 2))