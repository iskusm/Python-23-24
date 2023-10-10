
#for i in range(1, 11):
#    print(i)

for talet in range(1, 51):
    if talet % 3 == 0 and talet % 5 == 0:  # talet delbar med både 3 och 5
        print("FizzBuzz")
    elif talet % 3 == 0:     # talet delbar med 3
        print("Fizz")
    elif talet % 5 == 0:   # talet delbar med 5
        print("Buzz")
    else:
        print(talet)
