"""
tal = [7, 3, 18, 22, 2, 34]

minsta_tal = tal[0]

for i in tal:
    if i < minsta_tal:
        minsta_tal = i

print(f"Minsta talet i listan är {minsta_tal}")
"""

tal = []  # tom listan

for i in range(7):
    t = int(input("Ange ett tal: "))
    tal.append(t)

minsta_tal = tal[0]

for i in tal:
    if i < minsta_tal:
        minsta_tal = i

print(f"Minsta talet i listan är {minsta_tal}")
