"""Problema 6 - Ciclos
Diseñe una aplicación que permita ingresar n
números y muestre y sume los números
pares."""
#Contador
suma=0
#ingrea el total de numero que vas a sumar
N=int(input("Ingresa el total de numeros que vas a sumar: "))
#El total de veces que se va a repetir
for i in range(1,N+1):
	#Ingresa al numero
	sumN=int(input(f"Ingrese el {i} numero: "))
	#se va sumando
	suma+=sumN
#Muestra el total
print(f"El total es de: {suma}")