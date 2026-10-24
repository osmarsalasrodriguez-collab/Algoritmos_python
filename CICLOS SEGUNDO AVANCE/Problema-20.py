# Problema 20: Una compañía fabrica focos de colores (verdes, blancos y rojos). Se desea contabilizar,
# de un lote de N focos, el número de focos de cada color que hay en existencia.

total_focos = int(input("¿Cuántos focos hay en total?: "))

# Contadores para cada uno de los colores
verdes = 0
blancos = 0
rojos = 0

for i in range(total_focos):
    color = input("Ingresa el color del foco (verde/blanco/rojo): ")
    
    # Comprobamos la cadena ingresada para saber qué contador incrementar
    if color == "verde":
        verdes = verdes + 1
    elif color == "blanco":
        blancos = blancos + 1
    elif color == "rojo":
        rojos = rojos + 1

print("Focos verdes:", verdes)
print("Focos blancos:", blancos)
print("Focos rojos:", rojos)