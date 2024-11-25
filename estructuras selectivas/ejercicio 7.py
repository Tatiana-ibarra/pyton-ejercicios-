puntaje_matematica = float(input("Ingresa el puntaje de Aptitud Matemática: "))
puntaje_lenguaje = float(input("Ingresa el puntaje de Lenguaje: "))

if puntaje_matematica > puntaje_lenguaje:
    print("El estudiante obtuvo mayor puntaje en Aptitud Matemática.")
elif puntaje_lenguaje > puntaje_matematica:
    print("El estudiante obtuvo mayor puntaje en Lenguaje.")
else:
    print("El estudiante obtuvo puntajes iguales en ambas pruebas.")
