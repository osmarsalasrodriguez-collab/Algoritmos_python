# 18. Análisis de velocidad de vehículo:
# Evalúa la velocidad de 12 vehículos frente a un límite de 90 km/h,
# contando los que cumplen, las infracciones y las multas graves (>110 km/h).

cumplen = 0
infracciones = 0
graves = 0

# Evaluar los 12 vehiculos
for i in range(1, 13):
    vel = float(input("Velocidad del vehiculo " + str(i) + " (km/h): "))
    
    if vel <= 90:
        cumplen = cumplen + 1
    else:
        infracciones = infracciones + 1
        # Revisar si ademas es multa grave
        if vel > 110:
            graves = graves + 1

print("Vehiculos dentro del limite:", cumplen)
print("Total de infracciones:", infracciones)
print("Multas graves (>110 km/h):", graves)