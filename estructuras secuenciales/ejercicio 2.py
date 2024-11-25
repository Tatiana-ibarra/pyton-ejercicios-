area_inicial = float(input("Ingresa el área inicial de la cancha en metros cuadrados: "))
incremento = area_inicial * 0.20
area_total = area_inicial + incremento
print("\n--- Cálculo del Área Total ---")
print(f"Área Inicial: {area_inicial:.2f} m²")
print(f"Incremento (20%): {incremento:.2f} m²")
print(f"Área Total: {area_total:.2f} m²")
