def menu():
    print("Vad vill du göra?")
    print("===================")
    print("1. Lägga till eller ändra en address")
    print("2. Söka en address")
    print("3. Ta bort en address ur listan")
    print("4. Visa hela registret")
    print("0. Avsluta")

def lägga_till():
    namn = input("Ange ett namn: ")
    addr = input("Ange en address: ")
    register[namn] = addr

def söka_address():
    namn = input("Ange personens namn: ")
    if namn in register:
        print(register[namn])
    else:
        print(f"Det finns ingen person med namn {namn}")

def tabort_address():
    namn = input("Ange ett namn: ")
    if namn in register:
        del(register[namn])
    else:
        print(f"Det finns ingen person med namn {namn}")

def visa():
    for k, v in register.items():
        print(k, v)


def main():

    while True:
        menu()
        action = int(input("Välj 1-4 eller 0: "))
        
        if action == 0:
            break
        if action == 1:
            lägga_till()
        if action == 2:
            söka_address()
        if action == 3:
            tabort_address()
        if action == 4:
            visa()
        print("Tryck Enter för att fortsätta ...")
        

register = {}
main()
