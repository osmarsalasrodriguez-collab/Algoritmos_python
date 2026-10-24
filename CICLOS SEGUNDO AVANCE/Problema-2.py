# Problema 2: Mostrar la tabla de multiplicar de un n numero ingresado por teclado
#Ingresa un numero para que muestre la tabla de ese numero
num = int(input("Ingresa el numero: "))
#Se repite 10 veces
for i in range(1,11):
	#muestra el numero y tamnbien se multplica por i
	print(f"{num} x {i} = {num*i}")