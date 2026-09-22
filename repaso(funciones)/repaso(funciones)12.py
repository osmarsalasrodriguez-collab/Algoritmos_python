# Problema 12: Calificar una nota
# Regresa una letra según el rango de calificación del 0 al 100.
# --------------------------------------------------
#ingresa su calificacion
nota=int(input("ingresa tu calificacion: "))
def calificar(nota):
	#si es nota es mayor o igual que 90 aparece la letra A
	if (nota>=90):
		
		return "A"
	#si nota es mayor o igual que 80 y menor que 90 aparece la letra b
	elif (nota>=80 and nota<90): 
		
		return "B"
	#si nota es mayor o igual que 70 y menor o igual a 80 aparece la letra c
	elif(nota>=70 and nota<80):

		return "C"

	#Y si es menor que 70 sale la letra f
	else:
		return "F"

#resultado de la funcion
print(calificar(nota))
