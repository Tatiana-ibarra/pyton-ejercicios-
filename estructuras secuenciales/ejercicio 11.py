herencia_total = float(input("Ingresa el monto total de la herencia: "))
parte_madre = herencia_total * 0.5
parte_hijos = herencia_total * 0.5
parte_por_hijo = parte_hijos / 4

print("\n--- Distribución de la Herencia ---")
print(f"Total de la herencia: ${herencia_total:.2f}")
print(f"Parte de la madre: ${parte_madre:.2f}")
print(f"Parte de los hijos (en total): ${parte_hijos:.2f}")
print(f"Parte por cada hijo: ${parte_por_hijo:.2f}")
