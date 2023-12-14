def medelvärde(lst):
    return sum(lst) / len(lst)

list1 = [2, 4, 6, 7]
# print(medelvärde(list1))

# Skottår är det årtalet som delbar med 4 och 400
# men inte delbar med 100

def skottår(år):
    return år % 4 == 0 and år % 100 != 0 or år % 400 == 0

print(skottår(2024))
