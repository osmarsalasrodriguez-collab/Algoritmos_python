# 20. Procesamiento de facturas vencidas:
# Calcula recargos por mora en N facturas (5% si atraso >30 días, 12% si >60 días),
# mostrando cada factura actualizada y el total acumulado en penalizaciones.

n = int(input("Cuantas facturas vas a revisar?: "))
total_penalizaciones = 0

for i in range(1, n + 1):
    monto = float(input("Monto de la factura " + str(i) + ": "))
    dias = int(input("Dias de retraso: "))
    
    # Calcular recargo segun los dias de atraso
    if dias > 60:
        recargo = monto * 0.12
    elif dias > 30:
        recargo = monto * 0.05
    else:
        recargo = 0
        
    monto_final = monto + recargo
    total_penalizaciones = total_penalizaciones + recargo
    
    print("Factura", i, "con recargo:", round(monto_final, 2))

print("Total acumulado en penalizaciones:", round(total_penalizaciones, 2))