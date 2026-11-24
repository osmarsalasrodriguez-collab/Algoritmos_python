# 9. Simulador de pago de tarjeta de crédito:
# Calcula cuántos meses toma liquidar una deuda de $10,000 con interés
# mensual del 2% realizando abonos fijos de $1,000, y el total de intereses.

deuda = 10000
abono = 1000
meses = 0
total_intereses = 0

# Repetir mientras siga habiendo deuda
while deuda > 0:
    meses = meses + 1
    interes = deuda * 0.02 # Calcular 2% de interes mensual
    total_intereses = total_intereses + interes
    deuda = deuda + interes
    
    # Restar el abono (si la deuda es menor al abono, queda en 0)
    if deuda <= abono:
        deuda = 0
    else:
        deuda = deuda - abono

print("Meses para liquidar la deuda:", meses)
print("Total de intereses pagados:", round(total_intereses, 2))