# Programmet jämförar första och sista tecken
# i givna ordet.
'''
s1 = input('Skriv ett ord ')

if s1[0] == s1[-1]:
    print('Första och sista tecken är samma.')
else:
    print('Första och sista tecken är inte samma.')
'''

'''
Skapa en variabel som innehåller texten "pytonorm".
Använd sedan denna för att skapa tre ord som
innehåller texterna "ton", "norm" och "not".
'''

s3 = 'pytonorm'

print(s3[4:1:-1])
print(s3[7::-2])
print(s3[::-1])
