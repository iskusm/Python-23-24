# Python Dictionary (Ordbok)
dict_1 = dict()  # skapar en tom dictionary
dict_2 = {}

dict_3 = {"Kemi": "E", "Fysik": "D", "Matte": "E"}

dict_4 = {1: 3, 2: 4, 3: 2}

dict_5 = {"1984": ["George Orwell", 1950, "Secker and Warburg"],
          "Harry Potter": ["J.K.Rowling", "1997-2007","Tiden"]}
#print(dict_3)
#print(dict_4)
#print(dict_5)

for k, v in dict_3.items():
    print(k, v)

print(f"Dit betyg på fysik är {dict_3.get('Fysik')}")
