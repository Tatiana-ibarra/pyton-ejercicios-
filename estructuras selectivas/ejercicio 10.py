nombre = input("Ingresa el nombre: ")
edad = int(input("Ingresa la edad: "))
sexo = input("Ingresa el sexo (F para Femenino, M para Masculino): ").strip().upper()
estado_civil = int(input("Ingresa el estado civil (1: Casado, 2: Soltero, 3: Separado, 4: Otro): "))

if edad < 18:
    print(f"{nombre}, no puedes votar porque eres menor de edad.")
else:
    if sexo == "F":
        if estado_civil == 1:
            mesa = 1
        elif estado_civil == 2:
            mesa = 2
        elif estado_civil == 3:
            mesa = 3
        else:
            mesa = 4
    elif sexo == "M":
        if estado_civil == 1:
            mesa = 5
        elif estado_civil == 2:
            mesa = 6
        elif estado_civil == 3:
            mesa = 7
        else:
            mesa = 8
    else:
        print("Sexo inválido.")
        mesa = None

    if mesa:
        print(f"{nombre}, vota en la mesa {mesa}.")
