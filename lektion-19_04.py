def läs_tal():
    while True:
        try:
            s = input("Skriv ett tal: ")
            tal = float(s)
            return tal
        except ValueError:
            print("Felaktiga tal:", s)
            print("Försök igen")


x = läs_tal()
print(f"Talet i kvadrat är {x*x}")
