namn = "user1"
password = "qwerty"

input_name = input("Användarnamn: ")

while input_name != namn:
    print("Felaktigt användarnamn. Försök igen.")
    input_name = input("Användarnamn: ")

print(f"OK! Välkommen {namn}.")
