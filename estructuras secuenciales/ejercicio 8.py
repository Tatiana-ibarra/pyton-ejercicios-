costo_llamada1_operador1 = float(input("Ingresa el costo de la primera llamada al operador 1: "))
costo_llamada2_operador1 = float(input("Ingresa el costo de la segunda llamada al operador 1: "))
costo_llamada1_operador2 = float(input("Ingresa el costo de la primera llamada al operador 2: "))
costo_llamada2_operador2 = float(input("Ingresa el costo de la segunda llamada al operador 2: "))

total_operador1 = costo_llamada1_operador1 + costo_llamada2_operador1
total_operador2 = costo_llamada1_operador2 + costo_llamada2_operador2
total_llamadas = total_operador1 + total_operador2

print("\n--- Detalle de los Costos de las Llamadas ---")
print(f"Costo llamada 1 (Operador 1): ${costo_llamada1_operador1:.2f}")
print(f"Costo llamada 2 (Operador 1): ${costo_llamada2_operador1:.2f}")
print(f"Costo llamada 1 (Operador 2): ${costo_llamada1_operador2:.2f}")
print(f"Costo llamada 2 (Operador 2): ${costo_llamada2_operador2:.2f}")
print(f"Total llamadas Operador 1: ${total_operador1:.2f}")
print(f"Total llamadas Operador 2: ${total_operador2:.2f}")
print(f"Total de las cuatro llamadas: ${total_llamadas:.2f}")
