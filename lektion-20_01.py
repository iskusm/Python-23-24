# exempel på ordbok
katalog = {"Anders": 1234567899,
           "Berta": 3747384834,
           "Gerta": 28384773599}

# print(katalog["Berta"])

#for k, v in katalog.items():
#    print(f"{k}:  {v}")
"""
nytt_ordbok = {} # dict()

namn = input("Ange ett namn: ")
email = input("Ange email: ")

nytt_ordbok[namn] = email

print(nytt_ordbok)

# För att söka efter telefonnummer i ordbok "katalog"
if "Carl" in katalog:
    print(katalog["Berta"])
else:
    print(f"Ingen med namn Carl finns.")
"""
print("Vi skriver ut alla nycklar")
print(katalog.keys())
print("Vi skriver ut alla värde")
print(katalog.values())
print(katalog.get("Berta"))

# För att ta bort från ordbok
del(katalog["Berta"])
print(katalog)
