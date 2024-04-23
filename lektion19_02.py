import math

try:
    radius = float(input("Ange cirkelns radien: "))
except ValueError:
    print("Använd punkt istället komma tecken")
finally:
    radius = float(input("Ange cirkelns radien: "))
    omkrets = 2 * math.pi * radius
    arean = math.pi * radius * radius

    print(f"Cirkelns omkrets är {omkrets}")
    print(f"Cirkelns arean är {arean}")
