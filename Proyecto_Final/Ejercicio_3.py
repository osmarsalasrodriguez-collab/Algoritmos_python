# 3. Inversión con interés compuesto anual:
# Calcula el crecimiento anual de un capital inicial de $2000 al 8% de interés
# compuesto durante N años, mostrando ganancia por año y saldo final.

capital = 2000
tasa = 0.08
anios = int(input("Ingresa la cantidad de anios: "))

# Calcular la ganancia de cada anio y sumarla al capital
for i in range(1, anios + 1):
    ganancia = capital * tasa
    capital = capital + ganancia
    print("Anio", i, "- Ganancia:", round(ganancia, 2), "- Saldo:", round(capital, 2))

print("Saldo final acumulado:", round(capital, 2))