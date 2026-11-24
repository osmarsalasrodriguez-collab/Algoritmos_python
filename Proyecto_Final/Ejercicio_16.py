# 16. Validación e intentos de cobro en cajero:
# Simula un retiro en cajero permitiendo máximo 3 intentos fallidos
# (por clave incorrecta o saldo insuficiente) antes de cancelar la operación.

saldo = float(input("Ingresa el saldo inicial de la cuenta: "))
clave_correcta = "1234"
intentos = 0
retiro_exitoso = False

# Permitir intentar mientras no lleve 3 fallos ni haya retirado
while intentos < 3 and retiro_exitoso == False:
    clave = input("Ingresa tu clave: ")
    
    if clave != clave_correcta:
        intentos = intentos + 1
        print("Clave incorrecta. Intento", intentos, "de 3")
    else:
        monto = float(input("Cuanto deseas retirar?: "))
        if monto > saldo:
            intentos = intentos + 1
            print("Saldo insuficiente. Intento", intentos, "de 3")
        else:
            saldo = saldo - monto
            retiro_exitoso = True # Cambia a True para salir del ciclo
            print("Retiro exitoso! Nuevo saldo:", saldo)

if retiro_exitoso == False:
    print("Operacion cancelada por superar los 3 intentos.")0