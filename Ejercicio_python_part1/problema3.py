#Repaso - problema 3
# Un estacionamiento requiere determinar el cobro que debe aplicar 
# a las personas que lo utilizan. Considere que el cobro es con base 
# en las horas que lo disponen y que las fracciones de hora se toman como completas.
#--------------------------------------------------------------------------------------

#importa la funcion matematicas 
import math
#ingresa los minutos de estancia
minutos_estancia=float(input("Ingresa los minutos de estancia:  "))
#precio de hora
precio_hora=20
#math.ceil(), sirve para redondear un numero mayor o donde este mas cercano
redondeo=math.ceil(minutos_estancia/60)
cobro=precio_hora*redondeo
#resultado
print(f"Su pago es: {cobro}")
