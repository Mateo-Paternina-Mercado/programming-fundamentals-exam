import math

area = float(input("Enter the side of the equilateral triangle: "))

resultado = math.sqrt((3/4)*(area ** 2))

if resultado < 1000:
    print(f"""The area of the aquilateral triangle is {resultado}""")

elif resultado > 1000:
    print(f"""INVALID DATA""")       