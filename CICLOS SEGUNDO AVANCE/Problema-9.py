"""Problema 9 - Ciclos
Revisa la entrada de peso de 10 maletas en
un ciclo y cuenta cuántas superan el límite de
23 kg."""
#contador
MayorDe23=0
#se repite 10 veces
for i in range(1,11):
	#ingresa el peso
	peso=int(input(f"Ingresa el peso de la maleta {i}: "))
	#si es mayor a 23kg se va suma uno al MayorDe23
	if(peso>23):
		MayorDe23+=1

print(f"Maleta mayor de 23KG: {MayorDe23}")

