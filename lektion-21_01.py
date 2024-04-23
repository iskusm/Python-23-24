list_1 = [("Lisa", 18000), ("Anders", 21000),
          ("Birgit", 19000), ("Sandra", 16000)]

dict_1 = dict(list_1)
#print(type(dict_1))
#print(dict_1)

print(dict(sorted(dict_1.items(), key=lambda x: x[1])))

list_2 = ["Lisa", "Anders", "Birgit", "Sandra"]
list_3 = [18000, 21000, 19000, 16000]

dict_2= dict(zip(list_2, list_3))
print(dict_2)

