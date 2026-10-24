# Problema 5: Crea un programa que recorra los números del 1 al 20 e imprima
# únicamente aquellos que sean pares, indicando al final cuántos números pares se encontraron en total
#contador
contPares=0
#Se repite 20 veces
for i in range(1,21):
	#Si el resultado es igual a cero es par
	if i % 2 == 0:
		print(i)
		contPares+=1
#Muestra el total de pares
print(f"El total de pares son: {contPares}")