# 7. Registro de temperaturas extremas y promedios:
# Registra la temperatura diaria durante 30 días y determina
# la temperatura máxima, la mínima y el promedio mensual.

suma_temp = 0
temp_max = -999 # Valor inicial muy bajo para comparar
temp_min = 999  # Valor inicial muy alto para comparar

for dia in range(1, 31):
    temp = float(input("Temperatura del dia " + str(dia) + ": "))
    suma_temp = suma_temp + temp
    
    # Actualizar maxima y minima si corresponde
    if temp > temp_max:
        temp_max = temp
        
    if temp < temp_min:
        temp_min = temp

promedio = suma_temp / 30

print("Temperatura maxima:", temp_max)
print("Temperatura minima:", temp_min)
print("Promedio del mes:", round(promedio, 2))