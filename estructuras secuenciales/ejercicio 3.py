desempleo_inicial = float(input("Ingresa el valor inicial del desempleo en porcentaje: "))
aumento = desempleo_inicial * 0.095
desempleo_despues_aumento = desempleo_inicial + aumento
disminucion = desempleo_despues_aumento * 0.015
desempleo_actual = desempleo_despues_aumento - disminucion
print("\n--- Cálculo del Desempleo Actual ---")
print(f"Desempleo Inicial: {desempleo_inicial:.2f}%")
print(f"Aumento (9.5%): {aumento:.2f}%")
print(f"Desempleo después del Aumento: {desempleo_despues_aumento:.2f}%")
print(f"Disminución (1.5%): {disminucion:.2f}%")
print(f"Desempleo Actual: {desempleo_actual:.2f}%")
