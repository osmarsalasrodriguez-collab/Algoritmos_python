# 8. Rendimiento de un vehículo por trayecto:
# Calcula el rendimiento (km/l) en cada una de las 8 etapas de un viaje,
# además de la distancia total recorrida y el rendimiento promedio global.

total_km = 0
total_litros = 0

# Ciclo para las 8 etapas del viaje
for etapa in range(1, 9):
    km = float(input("Kilometros de la etapa " + str(etapa) + ": "))
    litros = float(input("Litros gastados en la etapa " + str(etapa) + ": "))
    
    rendimiento = km / litros
    print("Rendimiento etapa", etapa, ":", round(rendimiento, 2), "km/l")
    
    # Acumular totales para el promedio global
    total_km = total_km + km
    total_litros = total_litros + litros

rendimiento_global = total_km / total_litros

print("Distancia total recorrida:", total_km, "km")
print("Rendimiento promedio global:", round(rendimiento_global, 2), "km/l")