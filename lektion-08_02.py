# Exempel 2

# Programmet skriver ut talen 1- 20
# och deras kvadrater.
# Vi använder styrkoden "\t" för att få utskriften i
# kolumner

print("Kvadrattabell")
print("=============")
print("Tal \t Kvadrat")

i = 1

while i <= 20:
    print(i," \t ", i**2)
    i += 1    #i = i + 1
print("Här slutar while loop och fortsätter vanlig program.")
