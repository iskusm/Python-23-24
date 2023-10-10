## Grafik med `turtle`\-klassen

Här tar vi bara upp några av de mest grundläggande metoderna. Se [dokumentationen](https://docs.python.org/3.3/library/turtle.html?highlight=turtle) för en fullständig beskrivning. Turtlevärlden finns i modulen `turtle` som alltså måste importeras.

### Skapa

| Metod           | Funktion                                                                                      | Exempel             |
| --------------- | --------------------------------------------------------------------------------------------- | ------------------- |
| turtle.Turtle() | Skapar och returnerar en padda placerad i origo. Om det är första paddan skapas även världen. | t = turtle.Turtle() |

### Flytta och rita

| Metod             | Funktion                                                  | Exempel           |
| ----------------- | --------------------------------------------------------- | ----------------- |
| forward(n) fd(n)  | Gå `n` pixlar framåt.                                     |                   |
| backward(n) bk(n) | Gå `n` pixlar bakåt.                                      |                   |
| left(n) lt(n)     | Vrid `n` grader vänster.                                  |                   |
| right(n) rt(n)    | Vrid `n` grader höger.                                    |                   |
| goto(x, y)        | Gå till position `(x,y)`.                                 |                   |
| setx(x)           | Förflyttning i sidled.                                    |                   |
| sety(y)           | Förflyttning i höjdled.                                   |                   |
| setheading(n)     |                                                           |                   |
| seth(n)           | Sätter riktning. 0 är i x-axelns, 90 i y-axelns riktning. | t.seth(180)       |
| circle(radius)    | Gå i cirkel med angiven radie.                            |                   |
| dot(radius, col)  | Rita en punkt med angiven radie och färg.                 | t.dot(10, 'blue') |
| speed(n)          | Sätter farten.                                            |                   |

- 0 : snabbast, ingen animering

- 1 : långsamt

- 5

- 9 : snabbt
  
  |  |

### Hämta information om paddan

| Metod          | Funktion                                                        |
| -------------- | --------------------------------------------------------------- |
| towards(x,y)   | Returnerar riktningen till punkten (x,y).                       |
| xcor()         | Returnerar x-koordinaten.                                       |
| ycor()         | Returnerar y-koordinaten.                                       |
| heading()      | Returnerar kurs. 0 är positiva x-axeln, 90 är positiva y-axeln. |
| distance(x, y) | Returnerar avståendet till punkten (x,y).                       |
| distance(t)    | Returnerar avståendet till paddan t.                            |

### Kontroll av pennan, färger och fyllning

| Metod                                          | Funktion                                                  |
| ---------------------------------------------- | --------------------------------------------------------- |
| pendown()                                      |                                                           |
| pd()                                           | Kommer att rita.                                          |
| penup()                                        |                                                           |
| pu()                                           | Kommer ej att rita.                                       |
| pensize()                                      | Returnerar pennans storlek.                               |
| pensize(n)                                     | Sätter pennans storlek.                                   |
| isdown()                                       | True om pennan är nere, annars False.                     |
| pencolor(_colorstring_)                        | Sätter pennans färg. Exempel: `'blue'` eller `'#32c18f'`. |
| fillcolor(_colorstring_)                       | Sätter fyllningsfärg                                      |
| begin\_fill()                                  | Börjar fylla figurer.                                     |
| end\_fill()                                    | Slutar fylla figurer.                                     |
| clear()                                        | Tar bort allt paddan har ritat.                           |
| write(text, font=(name,size,type))             | Skriver en text. Exempel:                                 |
| `t.write('hej',   font=('Courier',24,'bold'))` |                                                           |
| hideturtle() ht()                              | Gör paddan osynlig.                                       |
| showturtle() st()                              | Gör paddan synlig.                                        |

Det finns metoder för att ändra storlek, form och färg på paddan. Det finns också metoder för att ändra fönstret (storlek, färg, koordinatsystem, ...) Se [dokumentationen](https://docs.python.org/3.3/library/turtle.html?highlight=turtle)!

[![Valid CSS!](http://jigsaw.w3.org/css-validator/images/vcss-blue)](http://jigsaw.w3.org/css-validator/check/referer)