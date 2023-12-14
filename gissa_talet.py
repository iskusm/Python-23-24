#!/usr/bin/python3.11
"""
 Author: Iskandarbek Usmanov
 Organisation: Hjalmar Strömerskolan
 Filename: gissa_talet.py
"""
# Gissa talet
import random

största_tal = int(input("Det största möjliga talet? "))
antal_försök = int(input("Hur många försök får man? "))

tal = random.randint(1, största_tal)

for i in range(antal_försök):
    gissning = int(input('Gissa talet? '))
    if gissning < tal:
        print('för litet')
    elif gissning > tal:
        print('för stort')
    else:
        print('rätt gissat')
        break
else:
    print('Inga fler försök')
    print('Talet var', tal)
