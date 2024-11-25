area_inicial = float(input("Ingresa el área inicial del terreno en metros cuadrados: "))
reduccion = area_inicial * 0.10
area_despues_reduccion = area_inicial - reduccion
incremento = area_despues_reduccion * 0.50
area_total = area_despues_reduccion + incremento
print("\n--- Cálculo del Área Total del Terreno ---")
print(f"Área Inicial: {area_inicial:.2f} m²")
print(f"Reducción (10%): {reduccion:.2f} m²")
print(f"Área después de la Reducción: {area_despues_reduccion:.2f} m²")
print(f"Incremento (50%): {incremento:.2f} m²")
print(f"Área Total: {area_total:.2f} m²")
