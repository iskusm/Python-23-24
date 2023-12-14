import random

största_tal = int(input("Största möjliga talet? "))
antal_försök = int(input("Antal försök: "))

talet = random.randint(1, största_tal)

for i in range(antal_försök):
    gissning = int(input("Gissa talet: "))

    if gissning < talet:
        print('för litet')
    elif gissning > talet:
        print('för stort')
    else:
        print("Rätt gissat.")
        break
else:
    print("Misslyckats. Ingen mer försök.")
    print("Talet var", talet)
