""" Un CRUD de pendientes"""
pendientes=['Configurar arduino IDE','Comprar una ESP32']
def listar_pendientes():
	for i in range(0,len(pendientes)):
		print(i+1,".-",pendientes[i])

def agregar_nuevo_pendiente():
	nuevo_pendiente=input("Cual es el nuevo pendiente?: ")
	if(len(nuevo_pendiente)==0):
		print("No oueden quedar espacios en blanco")
	else:
		pendientes.append(nuevo_pendiente)
		print("Pendiente agregado correctamente.")

#

while(True):
	print("\n------------------------------")
	print("0, -Teclea 0 si deseas salir. ")
	print("1.-Teclea 1 si deseas alistar  los pendientes")
	print("2,-Teclea 2 si deseas añadir un nuevo pendientes")
	print("3,-Teclea 3 si deseas editar un pendiente.")
	print("4,-Teclea 4 si deseas aguardar")
	print("\n------------------------------")

	try:
		opcion = int(input("Ingresa lo que deseas realizar: "))

		
		if(opcion==0):
			break
		elif(opcion==1):
			listar_pendientes()
		elif(opcion==2):
			agregar_nuevo_pendiente()


			listar_pendientes()
		elif(opcion==3):
			listar_pendientes()
			pendiente_a_modificar=int(input("¿Que pendidente desea modificar?: "))

			pendiente_seleccionado=pendientes[pendiente_a_modificar-1]
			print(f"Seleccionaste {pendiente_seleccionado} con que deseas reemplazarlo")
			nuevo_pendiente=input("¿Cual es el nuevo pendiente?: ")
			pendientes[pendiente_a_modificar-1]=nuevo_pendiente
		elif(opcion==4):
			with open("pendientes.txt","w",encoding="utf-8") as archivo:
				for pendiente in pendientes:
					archivo.write(f"{pendiente}\n")
		
	except:
		print("Debes elegir alguna de las opciones indicadas.")		

		
print("Espero tener pronto. ")