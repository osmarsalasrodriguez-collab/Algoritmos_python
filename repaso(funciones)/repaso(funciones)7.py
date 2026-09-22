# Problema 7: Verificar si es mayor de edad
# Regresa "Mayor" si la edad es 18 o más, de lo contrario "Menor".
# --------------------------------------------------
def es_mayor_de_edad(edad):
    # checamos si tiene 18 o mas
    if edad >= 18:
        return "Mayor"
    else:
        return "Menor"

# Pruebas
print(es_mayor_de_edad(17)) 
print(es_mayor_de_edad(18)) 
print(es_mayor_de_edad(45)) 