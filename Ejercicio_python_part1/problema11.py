# Repaso - problema 11
# Se requiere determinar cuál de tres cantidades proporcionadas es la mayor.
#------------------------------------------------------------------------------ 

#Ingresa las tres cantidades
a = int(input("Ingresa el primer numero: "))
b = int(input("Ingresa el segundo numero: "))
c = int(input("Ingresa el tercer numero: "))
#if para comparar las cantidades con un "and", para ver si es mayor o igual.
#si a es mayor o igual que b y c aparece que a es mayor
if a >= b and a >=c:
	print("El numero mayor es: ",a)
#si b es mayor o igual que a y c aparece que a es mayor
elif b >= a and b >= c:
	print("El numero mayor: ",b)
#si no c es mayor
else:
	print("El numero mayor es: ",c)



