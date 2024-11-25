area_total = float(input("Ingresa el área total del terreno en metros cuadrados: "))

area_cultivos = area_total * 0.40
area_vivienda = area_total * 0.25
area_zonas_verdes = area_total * 0.15
area_disponible = area_total - (area_cultivos + area_vivienda + area_zonas_verdes)

print("\n--- Distribución del Terreno ---")
print(f"Área para cultivos (40%): {area_cultivos:.2f} m²")
print(f"Área para vivienda (25%): {area_vivienda:.2f} m²")
print(f"Área para zonas verdes (15%): {area_zonas_verdes:.2f} m²")
print(f"Área disponible para otros proyectos: {area_disponible:.2f} m²")
