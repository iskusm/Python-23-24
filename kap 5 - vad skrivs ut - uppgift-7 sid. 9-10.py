#!/usr/bin/python3.11

"""
 Author: Iskandarbek Usmanov
 Organisation: Hjalmar Strömerskolan
 Filename: kap 5 - vad skrivs ut - uppgift-7 sid. 9-10.py

 Kurs: Programmering 1 (kurskod: PRRPRR01)
 Lärobok: Jan Sundström, Programmering 1 Python lärobok, Thelin Läromedel, 2016
 Arbetsbok: Jan Sundström, Programmering 1 Python arbetsbok, Thelin Läromedel, 2016
"""

# Vad skrivs ut?
x = 0

for i in range(10):
    x = x + 1
    for j in range(10):
        x = x + 1

print(x)
