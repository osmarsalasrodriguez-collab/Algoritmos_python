# Repaso - problema 8
# Almacenes "El harapiento distinguido" tiene una promoción: 
# a todos los trajes que tienen un precio superior a $2500.00 se les 
# aplicará un descuento de 15%, a todos los demás se les aplicará sólo 8%. 
# Realice un algoritmo para determinar el precio final que debe pagar una persona 
# por comprar un traje y de cuánto es el descuento que obtendrá.
#-----------------------------------------------------------------------------

#Ingresa el valor del traje
print("El herapiento distinguido")
val_traje=int(input("Ingresa el valor del traje: "))
#si el traje tiene valor mayor de 2500, te dan un 15% y si no el 8% de descuento
if(val_traje>2500.00):
	des=val_traje*0.15
	total=val_traje-des
else:
	
	des=val_traje*0.08
	total=val_traje-des
#resultado con el descuento que se te va aplicar y el total
print("El descuento es: ",des)
print("El total con descuento: ",total)