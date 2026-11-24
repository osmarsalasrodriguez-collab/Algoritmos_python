# 13. Control de producción por turnos:
# Registra las piezas producidas en tres turnos (Mañana, Tarde, Noche)
# durante 7 días, mostrando el total por turno y el turno más productivo.

manana = 0
tarde = 0
noche = 0

# Pedir piezas de cada turno durante los 7 dias
for dia in range(1, 8):
    print("--- Dia", dia, "---")
    p_manana = int(input("Piezas turno manana: "))
    p_tarde = int(input("Piezas turno tarde: "))
    p_noche = int(input("Piezas turno noche: "))
    
    manana = manana + p_manana
    tarde = tarde + p_tarde
    noche = noche + p_noche

print("Total manana:", manana)
print("Total tarde:", tarde)
print("Total noche:", noche)

# Comparar cual turno produjo mas
if manana > tarde and manana > noche:
    print("El turno mas productivo fue la Manana")
elif tarde > manana and tarde > noche:
    print("El turno mas productivo fue la Tarde")
else:
    print("El turno mas productivo fue la Noche")