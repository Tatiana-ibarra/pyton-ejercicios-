gol1 = int(input("Ingresa los goles anotados en el primer encuentro: "))
gol2 = int(input("Ingresa los goles anotados en el segundo encuentro: "))
gol3 = int(input("Ingresa los goles anotados en el tercer encuentro: "))
gol4 = int(input("Ingresa los goles anotados en el cuarto encuentro: "))

total_goles = gol1 + gol2 + gol3 + gol4

if total_goles > 10:
    promedio = total_goles / 4
    print(f"El promedio de goles es: {promedio:.2f}")
else:
    print("No se pide determinar el promedio")
