"""Problema 7 - Ciclos
Un sensor en la puerta de una discoteca
registra la edad de 8 personas que intentan
entrar. Usa un contador para determinar
cuántas personas son menores de edad
(menores a 18 años)."""
#contadores
mayEdad=0
menEdad=0
#se repite 8 veces
for i in range(1,9):
	#Ingresa la edad
	edad=int(input(f"Ingresa la edad de persona {i}: "))
	#si es es mayor o igual a 18 se va al contador de mayEdad, si no a menEdad
	if(edad>=18):
		mayEdad+=1
	else:
		menEdad+=1

print(f"Personas mayor de edad {mayEdad}")
print(f"Personas menores de edad {menEdad}")

