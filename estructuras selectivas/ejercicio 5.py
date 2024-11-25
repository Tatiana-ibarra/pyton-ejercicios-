nota = float(input("Ingresa la nota (entre 0.0 y 5.0): "))

if 4.6 <= nota <= 5.0:
    print("Excelente")
elif 3.6 <= nota < 4.6:
    print("Buena")
elif 3.0 <= nota < 3.6:
    print("Aceptable")
elif 2.0 <= nota < 3.0:
    print("Insuficiente")
elif 0.0 <= nota < 2.0:
    print("Deficiente")
else:
    print("Nota fuera de rango.")
