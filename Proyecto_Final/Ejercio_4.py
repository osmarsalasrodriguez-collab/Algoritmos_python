# 4. Plan de ahorro mensual con meta variable:
# Registra 12 depósitos mensuales, muestra el acumulado mes a mes
# y evalúa si al final del año se alcanzó la meta de $12,000.

meta = 12000
ahorro = 0

# Pedir el deposito de cada uno de los 12 meses
for mes in range(1, 13):
    deposito = float(input("Deposito del mes " + str(mes) + ": "))
    ahorro = ahorro + deposito
    print("Ahorro acumulado hasta el mes", mes, ":", ahorro)

print("Total ahorrado en el anio:", ahorro)

# Revisar si se cumplio la meta
if ahorro >= meta:
    sobrante = ahorro - meta
    print("Meta alcanzada! Te sobraron:", sobrante)
else:
    faltante = meta - ahorro
    print("No se alcanzo la meta. Faltaron:", faltante)