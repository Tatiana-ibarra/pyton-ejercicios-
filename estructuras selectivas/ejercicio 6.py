bonificacion = float(input("Ingresa el monto de la bonificación: "))

if bonificacion < 50000:
    dispositivo = "una cámara web"
elif 50000 <= bonificacion <= 200000:
    dispositivo = "un subwoofer"
elif 200000 < bonificacion <= 500000:
    dispositivo = "un disco duro externo"
elif 500000 < bonificacion <= 1000000:
    dispositivo = "una impresora multifuncional"
else:
    dispositivo = "un proyector"

print(f"Con la bonificación recibida, deberías comprar {dispositivo}.")
