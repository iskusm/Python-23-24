#!/usr/bin/python3.11

"""
 Author: Iskandarbek Usmanov
 Organisation: Hjalmar Strömerskolan
 Filename: kap 5 - celcius till farenheit - uppgift-10 sid. 10.py

 Kurs: Programmering 1 (kurskod: PRRPRR01)
 Lärobok: Jan Sundström, Programmering 1 Python lärobok, Thelin Läromedel, 2016
 Arbetsbok: Jan Sundström, Programmering 1 Python arbetsbok, Thelin Läromedel, 2016
"""

# Programmet omvandlar Celcius till Farenheit

celcius = 40

print("Celcius\tFarenheit")

while celcius >= -40:
    farenheit = 32 + celcius * 9/5
    print(f"{celcius:4d} \t {farenheit:6.1f}")
    celcius -= 1
    
