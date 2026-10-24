"""Problema 10 - Ciclos
Una discoteca tiene 8 personas registradas.
Usa un contador para determinar cuántas
personas son menores de edad (menores a
18 años)."""
#Arreglos
p_d=[20, 22, 14, 6, 15, 8, 18, 16,]
#Contador
contador=0
#Se repite por 8 veces
for i in range(8):
	#Si es menor a 18 se suma uno al contador
		if (p_d[i]<18):
		contador+=1
		print(f"La persona de edad: {p_d[i]} es menor de edad")

print(f"El total personas menores de edad es:{contador}")