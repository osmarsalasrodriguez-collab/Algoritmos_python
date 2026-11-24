# 6. Control de peso y sobrepeso en envíos:
# Evalúa el peso de N paquetes, aplica un recargo de $50 a los que superen 15 kg
# y muestra el total de paquetes con sobrepeso, recargos y peso promedio.

n = int(input("Numero de paquetes: "))
sobrepeso = 0
total_recargos = 0
suma_pesos = 0

for i in range(1, n + 1):
    peso = float(input("Peso del paquete " + str(i) + " (kg): "))
    suma_pesos = suma_pesos + peso
    
    # Aplicar recargo si pasa de 15 kg
    if peso > 15:
        sobrepeso = sobrepeso + 1
        total_recargos = total_recargos + 50

promedio = suma_pesos / n

print("Paquetes con sobrepeso:", sobrepeso)
print("Total de recargos:", total_recargos)
print("Peso promedio:", round(promedio, 2), "kg")