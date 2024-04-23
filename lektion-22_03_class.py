class BankKonto:
    def __init__(self, kontonummer, saldo, ägare):
        self.kontonummer = kontonummer
        self.saldo = saldo
        self.ägare = ägare
    
    def visaInfo(self):
        print("Saldo:", self.saldo)
    
    def sättain(self, belopp):
        self.saldo += belopp
        
    

sparkonto = BankKonto("123456789", 10000, "Max")
sparkonto.visaInfo()

sparkonto.sättain(5000)
sparkonto.visaInfo()

