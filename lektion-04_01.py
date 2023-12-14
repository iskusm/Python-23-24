namn = "Anders"  # personens namn
ålder = 23  # personens ålder
yrkes = "Lärare"  # personens yrke

# Gammal formaterings metoden som kommer från Python 2
print("%s är %d år gammal." % (namn, ålder))
# Sträng format metoden kom från Python 3.0
print("{} är {} år gammal.".format(namn, ålder))
# Nyaste sträng format metoden kom från Python 3.6
print(f"{namn} är {ålder} år gammal.")
