simbolo = input("Ingresa el símbolo químico: ").strip().capitalize()

if simbolo == "H":
    print("El símbolo corresponde al elemento Hidrógeno.")
elif simbolo == "O":
    print("El símbolo corresponde al elemento Oxígeno.")
elif simbolo == "N":
    print("El símbolo corresponde al elemento Nitrógeno.")
else:
    print("Elemento no encontrado.")
