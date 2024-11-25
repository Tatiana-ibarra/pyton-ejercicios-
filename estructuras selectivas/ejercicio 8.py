a = float(input("Ingresa la longitud del lado A: "))
b = float(input("Ingresa la longitud del lado B: "))
c = float(input("Ingresa la longitud del lado C: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Es un triángulo equilátero.")
    elif a != b and a != c and b != c:
        print("Es un triángulo escaleno.")
    else:
        print("Es un triángulo isósceles.")
else:
    print("Los lados no forman un triángulo válido.")
