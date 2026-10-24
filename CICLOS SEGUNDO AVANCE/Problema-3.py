# Problema 3: Pide al usuario que ingrese 5 números enteros uno por uno.
# Al finalizar la lectura, muestra la suma total de todos los números ingresados
#contador es igual a 0
suma=0
#Se repite por 5
for i in range(1,6):
	#ingresa el numero que quieres que se vaya sumando
	num = int(input(f"Ingresa el {i}: "))
	#El numero se va sumando al contador
	suma+=num
#El contador muestra el total
print(f"La suma total es de: {suma}")