total_tiempo = 0
total_distancia = 0

for dia in range(1, 4):
    tiempo = float(input(f"Ingresa el tiempo (en minutos) del día {dia}: "))
    distancia = float(input(f"Ingresa la distancia (en metros) recorrida el día {dia}: "))
    total_tiempo += tiempo
    total_distancia += distancia

promedio_tiempo = total_tiempo / 3
promedio_distancia = total_distancia / 3

print("\n--- Resumen del Entrenamiento ---")
print(f"Total tiempo entrenado durante la semana: {total_tiempo:.2f} minutos")
print(f"Total distancia recorrida durante la semana: {total_distancia:.2f} metros")
print(f"Promedio tiempo por día: {promedio_tiempo:.2f} minutos")
print(f"Promedio distancia por día: {promedio_distancia:.2f} metros")

