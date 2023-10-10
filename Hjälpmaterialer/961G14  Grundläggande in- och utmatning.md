## 961G24 Programmering i text-baserad miljö

### Grundläggande in- och utmatning

## In- och utmatning

Det första som man bör lära sig när det kommer till programmering är in- och utmatning. D.v.s. ett par simpla handgrepp för att få ut data på skärmen (som presenteras för den som kör programmet) och att få in data från tangentbordet (som användaren matar in genom att skriva på tangentbordet).

Varför är detta väsentligt? Jo, för att det är svårt att jobba om man inte kan se vad man gör (utmatning) och det är svårt att jobba om man inte har något data att jobba med (inmatning). Vi börjar därför med det simplaste python-programmet vi kan tänka oss. Programmet har endast ett kommando (en sats), på en enda rad:

```python
print('Hejsan Svejsan')
```

## Print

_print_ är alltså det kommando, den rutin, den funktion (kärt barn har många namn) som skriver ut data på skärmen. Funktionen print behöver få data för att veta vad den skall skriva ut, det är det som står inom parenteserna. I detta fall vill vi skriva ut en _sträng_, d.v.s. text, och för att markera detta använder vi enkla citationstecken kring den text som skall ut på skärmen. Citationstecknen är viktiga för de visar ju att _Hejsan Svejsan_ **inte** är något specifikt kommando eller så, utan exakt den text som vi vill ska dyka upp när vi kör programmet.

**Körexempel:**

```python
Hejsan Svejsan
```

Vi kommer framöver använda sådana "körexempel" när vi vill visa exakt hur något ser ut, eller skall se ut när programmet körs.

Print kan faktiskt hantera många olika typer av data, inte bara strängar, och vi skulle kunna skriva ut många saker om vi vill:

```python
print(100)
print(3.14)
print('3.14')
```

Då får vi ut följande på skärmen:

```
100
3.14
3.14
```

Observera att de två sista satserna i programmet resulterar i samma sak. Även om den första skriver ut ett decimaltal (eller flyttal som vi kommer att kalla dem) och det andra skriver ut en sträng.

Något mer man kan observera är att man automatiskt för en ny rad för varje print. Om man inte vill ha det så får man skriva det explicit:

```python
print('Hejsan ', end='')
print(100)
```

Då får vi följande resultat:

```
 Hejsan 100
```

## Input

Antag nu att man skulle vilja ha lite dialog med programmet. Vi vill att användaren skall få en chans att få mata in något, som sedan upprepas så att vi ser att det blivit rätt. Vi tänker oss ett program som ser ut ungefär så här:

**Körexempel:**

```
Hejsan!
Mata in ett heltal: 27
Du matade in heltalet 27
```

Första biten är enkel, det är ju två simpla print-satser. Men hur får vi sedan programmet att stanna? Den första "27":an är ju det som användaren matar in, d.v.s. skriver på tangentbordet. Den andra "27":an skrivs ut av datorn, d.v.s. programmet.

Här får vi ta hjälp av satsen input. Det är en sats som stannar programmet och väntar på att användaren matar in något på tangentbordet. Input väntar tills användaren har tryckt enter. Input är också kapabel till att skriva ut lite text innan användaren får börja mata in (ungefär som print). Vårt program skulle alltså kunna se ut så här:

```python
print('Hejsan!')
input('Mata in ett heltal: ')
```

Detta program går att köra, och det väntar faktiskt på inmatning. Men efter att användaren har matat in så händer inte så mycket. Det beror på att vi måste på något sätt lagra det som användaren matar in. I nuläget tar man emot det, men sparar det aldrig. För att göra detta behöver vi använda en _variabel_. En variabel är en lite bit av datorns minne som vi har reserverat för att spara något data. En variabel har alltid tre saker: Ett namn (väljer vi själva), ett värde (sätts första gången vi stoppar in något i minnesutrymmet) och en _datatyp_. Det sistnämnda kommer vi tillbaka till om en stund.

Vi kan nu fixa till vårt program:

```python
print('Hejsan!')
x = input('Mata in ett heltal: ')
```

_x_ är alltså namnet på vår variabel. Vi kan tänka på den som en liten låda, vari vi kan lagra något. I vårt program kommer lådan fyllas med det data som användaren matar in. Nu vill vi upprepa det inmatade datat tillbaka till användaren. Det kan vi göra på följande sätt:

```python
print('Hejsan!')
x = input('Mata in ett heltal: ')
print('Du matade in ', end='')
print(x)
```

print kan alltså också hantera att vi skickar en variabel till den. Då kommer värdet av variabeln att skrivas ut! Om vi nu kör programmet så blir det exakt som i vårt önskade körexempel ovan.

## Datatyper och tilldelning

Om man skall vara petig här så skall det nämnas att x faktiskt inte är ett heltal. Anledningen till detta är att input sparar allt som text, d.v.s. strängar. Detta kan man testa själv genom att försöka räkna med x, något som fungerar som förväntat med heltal, men inte alltid går med strängar. Antag nu att vi stoppar in en till variabel y:

```python
print('Hejsan!')
x = input('Mata in ett heltal: ')
print('Du matade in ', end='')
y = x - 1
print(y)
```

Satsen "y = x - 1" kallas för en _tilldelning_. Här beräknar vi ett värde på högersidan och stoppar in det i variabeln y. Om y hade existerat sedan tidigare skrivs ys gamla värde över. Om x vid ögonblicket för tilldelningen var 27 så borde y bli 26. Testar man detta program så kommer man få ett konstigt felmeddelande. Python klagar över något om operandernas typer. Det som har hänt här är att man försöker att utföra subtraktion på en sträng (x) och ett heltal 1, vilket inte är tillåtet. Matematiska operationer kräver att operanderna har samma datatyper.

Hur löser vi då detta? Jo vi får konvertera mellan datatyperna. Om man vill göra om något till ett heltal så använder man funktionen **int**. Det finns motsvarande funktioner för att konvertera till strängar (str) och flyttal (float).

```
print('Hejsan!')
x = int(input('Mata in ett heltal: '))
print('Du matade in ', end='')
y = x - 1
print(y)
```

Det som nu händer på andra raden är att det som vi får från input direkt görs om till ett heltal. D.v.s. strängen "27" görs om till heltalet 27, med vilket vi kan utföra aritmetik, så y blir 26 ett par rader längre ner.

### Strängsammanslagning

I ärlighetens namn så kan man faktiskt "plussa" strängar, men då handlar det om att slå ihop två strängar till en. Titta på följande exempel:

```python
ord1 = 'Drottning'
ord2 = 'Sylt'
ord3 = ord1 + ord2
print(ord3)
```

... på skärmen kommer "DrottningSylt".

## Övningar

**Uppgift 1**

Skriv ett program som låter användaren mata in två ord. Programmet skall sedan mata ut orden i omvänd ordning.

**Körexempel:**

```python
Mata in första ordet: Kalle
Mata in andra ordet: Bella
Du matade in Bella och Kalle
```

**Uppgift 2**

Skriv ett program som låter användaren mata in två heltal. Programmet skall sedan mata ut summan av de två heltalen.

**Körexempel:**

```python
Mata in ett heltal: 15
Mata in ett till: 17
Summan blev 32.
```

**Uppgift 3**

Skriv ett program som låter användaren mata in tre flyttal som vi kallar för A, B och C. Programmet skall sedan beräkna och mata ut

```python
5 * (A + B) * C
```

**Körexempel:**

```python
Mata in A: 1.5
Mata in B: 2.5
Mata in C: 3.33
Resultatet blev: 66.6
```

## Format

Det blir snart lite tradigt att sitta och skriva en print för vartenda litet data som skall skrivas ut på skärmen. Ett alternativ är att _formatera_ en sträng. Antag att vi som i uppgift 2 ovan har två variabler ord1 och ord2, innehållande strängarna "Kalle" resp. "Bella". Då kan vi göra utskriften för uppgiften med en enda rad:

```python
print('Du matade in {1} och {0}.'.format(ord1, ord2))
```

I strängen ovan är {1} och {0} _markörer_ får något som skall stoppas in. Det som skall stoppas in är det som kommer i paranteserna till funktionen format. Värdet i variabeln ord1 kommer stoppas in på 0-markören och värdet i variabeln ord2 kommer stoppas in i 1-markören (python börjar alltid räkna från 0, inte 1). Detta hade fungerat även om ord1 och ord2 var heltal eller någon annan datatyp.

Det som är extra bra med denna metod är att vi kan påverka formatet explicit på det som vi matar ut. Säg t.ex. att vi skulle vilja högerjustera utskriften av heltal med 7 teckens bredd. T.ex. om man skulle vilja göra ungefär så här:

**Körexempel:**

```python
Dina tal:
      5
    123
     64
```

Detta kan vi göra med en enda rad:

```python
print('{0:7}\n{1:7}\n{2:7}'.format(5,123,64))
```

Som tidigare anger vi inom klamrarna vilken av formats tal som vi vill ha, men vi kan också ange ":7" som innebär 7 teckens bredd för högerjustering. Vi använder '\\n' var att manuellt stoppa in radbrytningar. Vill man högerjustera ord så får man använda ett '>' tecken, t.ex. ":>7".

Vi kan också använda format för att beskriva hur flyttal skall formateras när de skrivs ut. Antag t.ex. att vi vill ha följande beteende:

**Körexempel:**

```python
Mata in ett flyttal: 3.141592
Du matade in 3.14
```

Vi vill ju här inte förstöra värdet 3.141592, utan bara avrunda just vid själva utskriften. Detta kan vi göra så här:

```python
pi = float(input('Mata in ett flyttal: '))
print('Du matade in {0:0.3}'.format(pi))
```

I detta fall innebär 0.3 att vi vill högerjustera med 0 teckens bredd (detta innebär vänsterjustering) och att vi vill ha tre värdesiffror i svaret. Om vi istället vill ange exakt hur många decimaler vi vill ha så skriver vi även dit ett 'f' sist:

```python
print('Du matade in {0:0.3f}'.format(pi))
```

**Körexempel:**

```python
Du matade in 3.142
```

## Övningar

**Uppgift 4**

Skriv ett program där användaren får mata in ett flyttal, ett heltal och en sträng. Programmet skall sedan mata ut dessa värden högerjusterad, med en bredd på 12 tecken. Flyttalet skall alltid ha 2 decimaler.

**Körexempel:**

```python
Mata in ett flyttal: 212.1233
Mata in ett heltal: 67
Mata in ett ord: gurka

Dina data:
      212.12
          67
       gurka
```

## f-strängar

F-strängar är ett alternativ till att använda funktionen format. Det ser ut på ett liknande sätt som format men kan vara ett smidigare alternativ i vissa lägen. En f-sträng kommer automatiskt att formateras av python. För att markera att det är en f-strängen sätter man tecknet 'f' före strängen och de delar av strängen som skall formateras markeras med {}-parenteser (precis som funktionen format).

```python
name = "Erik"
print(f"Hejsan {name}")
```

Nar man kör koden ovan så får man:

```python
Hejsan Erik
```

Om man vill skriva ut heltal så kan man ange hur mycket plats man vill ge heltalet:

```python
bottles = 99
print(f"Antal flaskor:{bottles:4}")
```

När man kör koden ovan får man

```python
Antal flaskor:  99
```

(D.v.s. 2 blanksteg före 99. Själva talet 99 tar ju två platser också, totalt 4). Om man vill skriva ut flyttal så kan man ange plats och antal decimaler precis som när man använder funktionen format:

```python
mypi = 3.14
print(f"Min goda pi:{mypi:6.3f}")
```

När man kör koden ovan får man

```python
Min goda pi: 3.140
```

Alltså, ett blanksteg först och sedan talet (som i sig tar 5 platser ink. decimalpunkten). Precis som med format kan vi använda f-strängar för att skriva ut flera saker samtidigt:

```python
print(f"Dina tal:\n{5:7}\n{123:7}\n{64:7}")
```

När man kör koden ovan får man

```python
Dina tal:
      5
    123
     64
```

I detta exempel ser vi också att det inte måste vara variablers värden som vi skriver ut. Vi kan också skriva ut konstanter (som 5, 123 och 64 i exemplet ovan).

Sidansvarig: [Pontus Haglund](mailto:pontus.haglund@liu.se?subject=https://www.ida.liu.se/~961G14/matr/stoff/in_och_utmatning.sv.shtml "E-posta Pontus Haglund (pontus.haglund@liu.se)")  
Senast uppdaterad: 2020-09-10