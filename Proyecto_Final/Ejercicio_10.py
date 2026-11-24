# 10. Evaluación de grupo académico:
# Clasifica las calificaciones de N estudiantes en reprobados (<6),
# aprobados (6 a 8.9) y excelencia (>=9), y calcula el promedio general.

n = int(input("Cuantos alumnos son?: "))
reprobados = 0
aprobados = 0
excelencia = 0
suma_calif = 0

for i in range(1, n + 1):
    calif = float(input("Calificacion del alumno " + str(i) + ": "))
    suma_calif = suma_calif + calif
    
    # Clasificar segun la calificacion
    if calif < 6:
        reprobados = reprobados + 1
    elif calif < 9:
        aprobados = aprobados + 1
    else:
        excelencia = excelencia + 1

promedio = suma_calif / n

print("Reprobados:", reprobados)
print("Aprobados:", aprobados)
print("Excelencia:", excelencia)
print("Promedio del grupo:", round(promedio, 2)