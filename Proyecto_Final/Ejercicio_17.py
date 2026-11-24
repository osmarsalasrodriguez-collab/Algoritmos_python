# 17. Tabla de amortización simplificada:
# Genera el desglose mensual de un préstamo con abono fijo a capital
# e interés del 1.5% sobre saldo insoluto, mostrando cuota y saldo restante.
9
prestamo = float(input("Monto del prestamo: "))
meses = int(input("A cuantos meses?: "))

abono_capital = prestamo / meses # Lo que se paga fijo de deuda cada mes
saldo = prestamo

for mes in range(1, meses + 1):
    interes = saldo * 0.015 # Interes sobre lo que falta por pagar
    cuota = abono_capital + interes
    saldo = saldo - abono_capital
    
    print("Mes", mes, "- Cuota:", round(cuota, 2), "- Saldo restante:", round(saldo, 2))6-