---
aliases:
  - Python
  - if-sats
tags:
  - python
  - if-else
---
If-satsen i Python avgör om en viss kodsekvens ska köra eller inte beroende på om ett logiskt uttryck är uppfyllt.

## Vad är en If-sats i Python?

En if-sats är inom programmering en _villkorssats_ som styr vad som ska hända i programmet beroende på om ett villkor är uppfyllt eller ej. Om villkoret är uppfyllt, kommer if-satsen att utföra en eller flera operationer/kommandon, annars hoppa över koden och gå vidare i programmet.

![If-satsen Python](https://www.programmerapython.se/wp-content/uploads/2019/12/Python-If-sats.png)

Flödesschemat visar hur programmet startar och kommer fram till If-villkoret. Ifall If-villkoret är uppfyllt så går programmet vidare och utför en eller flera operationer, men ifall villkoret inte är uppfyllt så hoppar programmet över operationerna och går vidare.

All programmering bygger på villkor och det är if-satserna som styr programmet beroende på vad villkoren säger, vilket ger hela grunden för all logik i programmering!

**_Varje if-sats har ett villkor som kan besvaras med True eller False_.**

Varje if-sats har ett villkor, ett så kallat påstående som kan besvaras med sant, eller falskt (True eller False). Om villkoret är sant (True), kommer programmet gå in i if-satsen och utföra alla operationer som är specificerade inom blocket.

![](https://www.programmerapython.se/wp-content/uploads/2020/03/ifsats.png)

###### If-satsen i Python:

- Är en villkorssats som utför en eller flera operationer om villkoret är uppfyllt, (True).
- Styr all logik inom programmering.
- Villkoret (uttrycket) i if-satsen kan alltid besvaras med en boolean, det vill säga antingen sant eller falskt (True eller False).

## Hur gör man en If-sats i Python?

Man skapar en if-sats med syntaxten:

if (logiskt uttryck):

Operation/Operationer …

- Man deklarerar en if-sats enkelt med det reserverade ordet if.
- Alla rader som är indenterade (indrad) tillhör if-satsen.
- Alla rader som tillhör if-satsen kommer köra om if-satsens villkor är uppfyllt (True).
- Är villkoret True, kommer if-satsen köra.
- If-satsen är klar när man slutar indentera koden.

## Hur gör man en if-sats i Python – Exempel

I följande exempel visar vi hur en if-sats fungerar. All kod som har en indentering (indrag) tillhör if-satsen och kommer utföras om if-villkoret är uppfyllt (True). If-satsen är slut när indenteringen upphör. Om if-satsen aldrig blev uppfylld (False) så hoppar programmet över all kod som tillhör if-satsen (indenterad kod).

**Exempel:**

```python
run_operation = True 
if(run_operation):  
    print("If-satsen körs.")  
    print("Alla operationer som är indenterade, kommer att utföras.") 

print("Detta kommandot är inte med i if-satsen, eftersom koden inte är indenterad.")
```

Utskriften kommer i detta fall bli:

```python
If-satsen körs.
Alla operationer som är indenterade, kommer att utföras.
Detta kommandot är inte med i if-satsen, eftersom att koden inte är indenterad.
```

Om vi istället sätter variabeln run\_operation till False så kommer if-satsen inte köra koden.

```python
run_operation = False
if(run_operation):  
    print("If-satsen körs.")  
    print("Alla operationer som är indenterade, kommer att utföras.") 

print("Detta kommandot är inte med i if-satsen, eftersom koden inte är indenterad.")
```

Utskriften blir alltså:

```py
Detta kommandot är inte med i if-satsen, eftersom att koden inte är indenterad.
```

## Exempel på If-sats med flera villkor

Det är möjligt att ha flera villkor på samma gång i en if-sats. I tidigare kapitel lärde vi oss vanliga [Jämförelse- och Logiska Operatorer i Python](https://www.programmerapython.se/jamforelser-och-logiska-operatorer-i-python/) där vi såg de vanligaste jämförelseoperationerna som mindre än, större än och lika med (<, >, ==). Dessa jämförelser går att kombinera med flera villkor som exempelvis _and_ eller _or_.

**Exempel: Och-operationen**

I Python använder man sig av det reserverade ordet _and_ för att ange ett extra villkor _där **båda** villkoren måste vara sanna (True) för att if-satsen ska utföras_.

Om vi vill kontrollera ifall en int-variabel ligger inom ett intervall t.ex. mellan 0 _**och**_ 200, sätter vi enkelt upp en if-sats med det logiska uttrycket.

Är variabeln num större än 0 och mindre än 200 så får vi en utskrift, Number: num 

```py
num = 20 
if(num > 0 and num < 200):  
    print("Number:", num)
```

I detta fallet blir alltså utskriften  
Number: 20

**Exempel: Eller-operationen**

I Python använder man sig av det reserverade ordet _or_ för att ange ett extra villkor _där **något** av villkoren måste vara sann (True) för att if-satsen ska utföras_.

I följande exempel kommer if-satsen köra om variabeln _num_ är lika med 20 _**eller**_ om _num_ är lika med 10.

```py
num = 20 
if(num == 20 or num == 10):  
    print("Number:", num)
```

Utskriften blir alltså:

Number: 20

## If-satsen i Python – Vanliga frågor och svar

**Vad är en villkorssats?**

En villkorssats är en sats, som utför en operation enbart om ett villkor är uppfyllt, det vill säga True. Dessa satser kan exempelvis vara if-, else- eller else-if-satserna.

___

###### [Bakåt](https://www.programmerapython.se/if-satser-inledning/)    |    [Framåt](https://www.programmerapython.se/else/)