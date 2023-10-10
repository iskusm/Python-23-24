namn = "user1"
password = "qwerty"

i = 1

while i < 4:
    input_name = input("Användarnamn: ")
    if input_name != namn:
        print("Felaktigt användarnamn. Försök igen.")
        i += 1
    if input_name == namn:
        print(f"OK! Välkommen {namn}.")
        break

if i == 4:
    print("Inloggningen har låst till 15 minuter.")
