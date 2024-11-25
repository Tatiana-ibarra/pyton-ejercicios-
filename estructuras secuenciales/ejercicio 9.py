alto = float(input("Ingresa la altura del muro del baño en metros: "))
ancho = float(input("Ingresa el ancho del muro del baño en metros: "))
area_bano = alto * ancho
baldosas_necesarias = area_bano / 3.5

print("\n--- Cálculo del Área y Baldosas Necesarias ---")
print(f"Área del baño: {area_bano:.2f} m²")
print(f"Cantidad de baldosas necesarias: {baldosas_necesarias:.2f}")
