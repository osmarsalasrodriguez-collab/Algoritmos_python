# 15. Consumo de energía eléctrica y tarifas por escalón:
# Calcula el cobro de 6 bimestres aplicando tarifa base ($1.50/kWh) hasta
# 250 kWh y tarifa excedente ($2.80/kWh) al consumo adicional, más el gasto anual.

gasto_anual = 0

# Ciclo para los 6 bimestres del anio
for bimestre in range(1, 7):
    kwh = float(input("Consumo de kWh en el bimestre " + str(bimestre) + ": "))
    
    # Calcular cobro con tarifa normal o excedente
    if kwh <= 250:
        pago = kwh * 1.50
    else:
        extra = kwh - 250
        pago = (250 * 1.50) + (extra * 2.80)
       
    print("Pago del bimestre", bimestre, ":", round(pago, 2))
    gasto_anual = gasto_anual + pago

print("Gasto anual total:", round(gasto_anual, 2)