import random

# print(random.random())  # slumptal mellan 0 och 1

for i in range(10):
    # print(round(random.random(), 3))
    slumptal = random.random()
    #print(round(slumptal, 3))
    
# random.randint(nedre, övre)

# for i in range(10):
    #print(random.randint(1, 50))
    
# random.choice()

kort = ["spader", "klever", "hjarter", "rooter"]

print(kort)

random.shuffle(kort)
print(kort)

print(random.randrange(10, 20))
