'''El sistema de liquidación que hacen los conductores de buses y los colectivos a las 
diferentes empresas consiste en tomar un número de la registradora al iniciar el día y otro 
al terminarlo . La diferencia de estos dos números determina el numero de pasajeros 
transportados en el día. Realizar un algoritmo que permita leer estos dos números y el 
valor del pasaje. Calcular e imprimir el total de pasajeros, el valor liquidado al conductor y 
el total liquidado a la empresa. Tenga en cuenta que la empresa recibe tres cuartas partes 
del dinero mientras el conductor recibe el resto.'''
inicio = int(input("¿Cuál fue el número de la registradora al inicio del día? "))
final = int(input("¿Y el número de la registradora al final del día? "))
pasaje = float(input("¿Cuánto cuesta el pasaje? "))
pasajeros = final - inicio
dinero_total = pasajeros * pasaje
conductor = dinero_total * 0.25  # El conductor recibe el 25%
empresa = dinero_total * 0.75    # La empresa recibe el 75%
print("\nResultados del día:")
print(f"Total de pasajeros transportados: {pasajeros}")
print(f"El conductor recibe: ${conductor:.2f}")
print(f"La empresa recibe: ${empresa:.2f}")