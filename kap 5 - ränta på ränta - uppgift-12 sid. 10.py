#!/usr/bin/python3.11

"""
 Author: Iskandarbek Usmanov
 Organisation: Hjalmar Strömerskolan
 Filename: kap 5 - ränta på ränta - uppgift-12 sid. 10.py

 Kurs: Programmering 1 (kurskod: PRRPRR01)
 Lärobok: Jan Sundström, Programmering 1 Python lärobok, Thelin Läromedel, 2016
 Arbetsbok: Jan Sundström, Programmering 1 Python arbetsbok, Thelin Läromedel, 2016
"""
# Programmet beräknar hur mycket pengar man har på sitt sparkonto vid
# en årsränta på 2%, startkapital på 1 krona och efter 2017 år
print('Ränta på ränta')
print('===================')

# Deklarera variabler och dess värde
rent = 1.02
capital = 1.00

for year in range(1, 2018):
    capital *= rent
    print(f"År {year:4d} är kapitalet {capital:.0f} kr.")

print(f"År 2017 är kapitalet {1.02**2017:.0f} kr.")

input("\nTryck Enter för att avsluta...\n")
