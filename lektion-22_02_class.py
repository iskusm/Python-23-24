class Bil:
    def __init__(self, model, år, färg):
        self.model = model
        self.år = år
        self.färg = färg
    
    def visaInfo(self):
        print("Model:", self.model)
        print("År:", self.år)
        print("Färg:", self.färg)

    def move(self):
        print("Bilen startar")

# skapa ny bil model
volvo = Bil("Volvo Tundra", 1974, "vit")
volvo.visaInfo()
volvo.move()
