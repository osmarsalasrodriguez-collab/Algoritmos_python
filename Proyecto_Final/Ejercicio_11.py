# 11. Estadística de edades por rangos:
# Contabiliza cuántas personas de un grupo de N pertenecen a cada rango:
# niños (0-12), adolescentes (13-17), adultos (18-59) y adultos mayores (60+).

n = int(input("Numero de personas: "))
ninos = 0
adolescentes = 0
adultos = 0
mayores = 0

for i in range(1, n + 1):
    edad = int(input("Edad de la persona " + str(i) + ": "))
    
    # Contar segun el rango de edad
    if edad <= 12:
        ninos = ninos + 1
    elif edad <= 17:
        adolescentes = adolescentes + 1
    elif edad <= 59:
        adultos = adultos + 1
    else:
        mayores = mayores + 1

print("Ninos:", ninos)
print("Adolescentes:", adolescentes)
print("Adultos:", adultos)
print("Adultos mayores:", mayores)-*