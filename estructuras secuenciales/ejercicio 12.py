monto_herencia = float(input("Ingresa el monto total de la herencia: "))

monto_esposa = monto_herencia * 0.40
monto_hijo1 = monto_herencia * 0.30
monto_hijo2 = monto_herencia * 0.20
monto_hijo3 = monto_herencia * 0.40
monto_hijo4 = monto_herencia * 0.10

print("\n--- Distribución de la Herencia ---")
print(f"Esposa: ${monto_esposa:.2f}")
print(f"Hijo 1: ${monto_hijo1:.2f}")
print(f"Hijo 2: ${monto_hijo2:.2f}")
print(f"Hijo 3: ${monto_hijo3:.2f}")
print(f"Hijo 4: ${monto_hijo4:.2f}")
