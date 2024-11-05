voltage1 = int(input("Enter the first voltage: "))
voltage2 = int(input("Enter the second voltage: "))
voltage3 = int(input("Enter the third voltage: "))
voltage4 = int(input("Enter the room voltage: "))
voltage5 = int(input("Enter the fifth voltage: "))

promedio =(voltage1 + voltage2 + voltage3 + voltage4 + voltage5)/5

if promedio > 220:
    print(f"""{promedio} its voltage is high""")

elif promedio < 220: 
    print(f"""{promedio} its voltage is correct""")