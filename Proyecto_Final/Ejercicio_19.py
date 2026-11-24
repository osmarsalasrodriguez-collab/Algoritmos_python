# 19. Sensor de nivel de depósito con alerta:
# Registra descargas de líquido en un tanque de 1000 L hasta alcanzar o superar
# el 95% de capacidad, emitiendo una alerta y mostrando descargas y volumen final.

capacidad = 1000
limite_alerta = 950 # 95% de 1000 litros
volumen_actual = 0
descargas = 0

# Seguir pidiendo descargas mientras no llegue al limite
while volumen_actual < limite_alerta:
    descargas = descargas + 1
    litros = float(input("Litros de la descarga " + str(descargas) + ": "))
    volumen_actual = volumen_actual + litros
    print("Nivel actual del tanque:", volumen_actual, "L")

print("ALERTA: El tanque llego o supero el 95% de su capacidad!")
print("Total de descargas:", descargas)
print("Volumen final almacenado:", volumen_actual, "L")