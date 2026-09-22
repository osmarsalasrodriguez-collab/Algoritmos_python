# Problema 10: Operación básica
# Realiza suma, resta o multiplica según el texto dado.
# --------------------------------------------------

def operacion_basica(num1,num2, operacion):
	#Checa que operacion desea
	if (operacion == "suma"):
		#operacion de suma
		return num1+num2
	elif (operacion == "resta"): 
		#operacion de resta
		return num1-num2
	elif(operacion == "division"):
		#operacion de division
		return num1/num2

	elif(operacion=="multiplicacion"):
		#operacion de multiplicacion
		return num1*num2
	else:
		#si agrega un simbolo incoherente a lo que se pide
		return "No se puede"
#Prueba llamando dos numeros y la operacion que se desea
print(operacion_basica(2,6,"resta"))
print(operacion_basica(8,9,"suma"))
print(operacion_basica(9,6,"multiplicacion"))
print(operacion_basica(12,3,"division"))

