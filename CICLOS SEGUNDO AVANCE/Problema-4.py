# Problema 4: Pide al usuario que ingrese N números enteros uno por uno.
# Al finalizar la lectura, muestra la suma total de todos los números ingresados
#Ingresa la cantidad que desea que se repita
num =  int(input("Ingrese la cantidad: "))
#contador es igual a cero
suma=0
#Numero que repita
for i in range(1,num):
	#Ingresa el numero que se va a sumar
	N = int(input(f"Ingrese el {i} numero: "))
	#El numero se suma al contador
	suma+=N 
#muestra el resultado	
print(f"La suma total es: {suma}")