edad = int(input("Ingresa la edad de la persona: "))
tasa_cambio = float(input("Ingresa la tasa de cambio de dólares a pesos colombianos: "))

if 1 < edad < 4:
    costo = 0
elif 4 <= edad <= 8:
    costo = 2
elif 9 <= edad <= 16:
    costo = 5
elif 17 <= edad <= 35:
    costo = 6
else:
    costo = 10

costo_pesos = costo * tasa_cambio

print(f"El valor de la entrada es: ${costo} USD, equivalente a ${costo_pesos:.2f} COP.")
