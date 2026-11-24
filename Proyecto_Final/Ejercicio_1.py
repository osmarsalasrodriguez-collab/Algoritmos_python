# 1. Simulación de nómina semanal con horas extras:
# Calcula el sueldo semanal de un trabajador (6 días) pagando tarifa normal
# hasta 8 horas diarias y tarifa doble por cada hora extra trabajada.

tarifa = float(input("Ingresa la tarifa por hora: "))
horas_extras_totales = 0
sueldo_total = 0

# Ciclo para los 6 dias de la semana
for dia in range(1, 7):
    horas = float(input("Horas trabajadas en el dia " + str(dia) + ": "))
    
    # Separar horas normales de las extras
    if horas > 8:
        horas_normales = 8
        extras = horas - 8
    else:
        horas_normales = horas
        extras = 0
        
    horas_extras_totales = horas_extras_totales + extras
    pago_dia = (horas_normales * tarifa) + (extras * tarifa * 2) # Las extras se pagan al doble
    sueldo_total = sueldo_total + pago_dia

print("El sueldo total semanal es:", sueldo_total)
print("Total de horas extras:", horas_extras_totales)