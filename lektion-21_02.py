def lägg_till():
    namn = input("Ange namn: ")
    lön = int(input("Ange lön: "))

    if namn in dict_1:
        dict_1[namn] = lön
        print("Lön har ändrats.")
    else:
        dict_1[namn] = lön
        print("Ny anställda tilllagt.")


dict_1 = {"Anna": 21000}
lägg_till()
print(dict_1)
lägg_till()
print(dict_1)
