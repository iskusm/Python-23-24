## Beräkna biljettpriset på bussbiljetter

Du ska i denna uppgift hjälpa ett bussbolag med att skriva ett program som räknar ut biljettpriset för olika resenärer.

Följande specifikation är given:

-   En standardbiljett för en vuxen kostar 200 kr.
-   De som är under 18 år räknas som ungdomar och får därför 20% rabatt.
-   De som är över 65 år räknas som pensionär och får därför 30% rabatt.

Skapa ett program som frågar personen hur gammal han/hon är. Skriv sedan ut vad biljettpriset blir för denna person. Utgå från att användaren alltid ger ett heltal och alltid i rätt format. Om användaren anger ett negativt tal så ska ett felmeddelande skrivas ut.

### Ledtråd

Använd funktionen `input()` för att ta in ett värde från användaren. Läs mer om inputs i Python under avsnittet [input i Python](https://www.programmerapython.se/input-i-python/).

value = input("Ange ett värde: ")

value = input("Ange ett värde: ")

```
value = input("Ange ett värde: ")
```

**Exempel på procenträkning:** Om kostnaden är 500 och rabatten 10% blir det nya `500 * 0.9 = 450`.

### Lösning

**Svar:**

TICKET = 200

input = input("Ange din ålder: ")

input = int(input)

if input < 0:

print("Felaktig inmatning")

exit()

elif input < 18:

total\_price = TICKET \* 0.8

elif input \> 65:

total\_price = TICKET \* 0.7

else:

total\_price = TICKET

print(f"Biljettpriset blir: {total\_price} kr")

TICKET = 200 input = input("Ange din ålder: ") input = int(input) if input < 0: print("Felaktig inmatning") exit() elif input < 18: total\_price = TICKET \* 0.8 elif input > 65: total\_price = TICKET \* 0.7 else: total\_price = TICKET print(f"Biljettpriset blir: {total\_price} kr")

```
TICKET = 200

input = input("Ange din ålder: ")
input = int(input)
if input < 0:
    print("Felaktig inmatning")
    exit()
elif input < 18:
    total_price = TICKET * 0.8
elif input > 65:
    total_price = TICKET * 0.7
else:
    total_price = TICKET

print(f"Biljettpriset blir: {total_price} kr")

```

**Förklaring:**

Först anger vi grundpriset som en konstant: `TICKET = 200`. Vi frågar sedan användaren om en input och konverterar inputen till ett heltal `int(input)`. Notera att inputs i Python alltid har datatypen `string` och måste därför konverteras till en integer.

Vi använder till sist ett par if-satser för att möta specifikationen. Första if-satsen kollar om talet är negativt. I så fall stänger vi ner programmet med funktionen `exit()` som direkt avslutar programmet. I övriga fall beräknar vi totalpriset och skriver ut svaret.
---
