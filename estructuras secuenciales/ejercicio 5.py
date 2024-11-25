minutos = int(input("Ingresa la cantidad de minutos: "))
horas = minutos // 60
minutos_restantes = minutos % 60
print("\n--- Conversión de Minutos a Horas ---")
print(f"{minutos} minutos equivalen a {horas} horas y {minutos_restantes} minutos.")
