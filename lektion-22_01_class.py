class Matratt:
    def __init__(self, namn, pris, veggo):
        self.namn = namn
        self.pris = pris
        self.veggo = veggo

    def visaInfo(self):
        print("Namn:", self.namn)
        print("Pris:", self.pris, "kr")
        print("Vegetarisk?", self.veggo)

# Skapa en ny maträtt
bolognese = Matratt("Pasta bolognese", 80, False)

# Anropa metoden för att visa information om maträtten
bolognese.visaInfo()

pizza = Matratt("Pizza Asteka", 120, False)
pizza.visaInfo()
