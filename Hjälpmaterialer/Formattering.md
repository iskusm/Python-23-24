Att omvandla tal till text (strängar med siffror) kan göras på olika sätt. De två bästa sätten att konvertera värdet av `x` till en sträng är att använda en f-sträng eller att anropa metoden `format` i strängklassen.

### f-strängar

Antag att vi har satt två variabler `n` och `x` till 12 respektive 2/3 dvs. ett värde av heltals- och ett av flyttalstyp.

Exempel på konvertering med dessa tal:

| Kod                        | Värde                               |
| -------------------------- | ----------------------------------- |
| f'{n}'                     | '12'                                |
| f'n = {n}'                 | 'n = 12'                            |
| f'{n} i kvadrat är {n\*n}' | '12 i kvadrat är 144'               |
| f'{x}'                     | '0.6666666666666666'                |
| f'x i kvadrat är {x\*\*2}' | 'x i kvadrat är 0.4444444444444444' |

I f-strängar kan man alltså skriva ett uttryck inom klammerparenteser. Dessa uttryck evalueras till ett värde som sedan konverteras till en sträng.

Det går att specificera detaljer som fältbredd och antal decimaler genom att skriva en _formatkod_.

Exempel med samma `n` och `x` som ovan men med formatkoder:

| Kod          | Värde         | Kommentar                                           |
| ------------ | ------------- | --------------------------------------------------- |
| f'{n:6d}'    | ' 12'         | Heltal, 6 positioner, högerjusterat.                |
| f'{n:<6d}'   | '12 '         | Heltal, 6 positioner, vänsterjusterat.              |
| f'{n:^6d}'   | ' 12 '        | Heltal, 6 positioner, centrerat.                    |
| f'{x:.3f}'   | '0.667'       | Flyttal, 3 decimaler.                               |
| f'{x:10.4f}' | ' 0.6667'     | Flyttal,4 decimaler, högerjusterat i 10 positioner. |
| f'{x:.5e}'   | '6.66667e-01' | Flyttal på exponentform, 5 decimaler.               |

Således:

- Formatkoderna skrivs efter kolon inom klamrarna.
- Koden `d` anger heltal på decimal form.
- Koden `f` anger flyttal på decimal form.
- Koden `e` anger flyttal på exponentform.
- Fältets bredd kan anges efter bokstavskoden.
- Positionering i fältet kan specificeras med `<` och `^`. Högerjustering är default men kan också anges med `>`.
- För flyttal kan antal decimaler specificeras efter en punkt.

### Metoden `format`

Samma exempel som med f-strängar ovan:

| Kod                                  | Värde                 |
| ------------------------------------ | --------------------- |
| '{}'.format(n)                       | '12'                  |
| 'n = {}'.format(n)                   | 'n = 12'              |
| '{} i kvadrat är {}'.format(n, n\*n) | '12 i kvadrat är 144' |
| '{}'.format(x)                       | '0.6666666666666666'  |
| '{:6d}'.format(n)                    | ' 12'                 |
| '{:<6d}'.format(n)                   | '12 '                 |
| '{:^6d}'.format(n)                   | ' 12 '                |
| '{:.3f}'.format(x)                   | '0.667'               |
| '{:10.4f}'.format(x)                 | ' 0.6667'             |
| '{:.5e}'.format(x)                   | '6.66667e-01'         |

Här anger man alltså värdena som användas som parametrar till `format`\-metoden. Även här kan man ange formatkoder efter kolontecknet i _platshållaren_ `{}`.

### Formatering med `%`\-operatorn

Exempel:

| Kod                          | Värde              |
| ---------------------------- | ------------------ |
| 'n = %d, x = %5.2f' % (n, x) | 'n = 12, x = 0.67' |

Här skrivs formatkoderna efter `%` inuti strängen. Tecknet `%` används också som operator mellan en sträng och en tupel.

Detta är ett föråldrat sätt att göra formatkonverteringar, men man bör i alla fall förstå vad det är när man ser det.