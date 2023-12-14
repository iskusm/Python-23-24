#!/usr/bin/python3.11

# Nästlade for-satser
rader = int(input("Antal rader: "))

for i in range(rader, 0, -1):
    for j in range(1, i+1):
        print('*', end='')
    print()   # för att avsluta raden
