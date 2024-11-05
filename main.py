voltaje1 = float(input("Ingresa el primer voltaje: "))
voltaje2 = float(input("Ingresa el segundo voltaje: "))
voltaje3 = float(input("Ingresa el tercer voltaje: "))

promedio = (voltaje1 + voltaje2 + voltaje3) / 3

if promedio < 115:
    print("VOLTAJE CORRECTO")
elif 115 <= promedio < 220:
    print("ALTO VOLTAJE")
else:
    print("PELIGRO")