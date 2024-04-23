import math

def medel_värde(alist):
    sum = 0
    for elem in alist:
        sum = sum + elem
    return sum / len(alist)

def main():
    try:
        s = input("Skriv ett antal tal: ")
        ls = s.split()
        tlist = [float(t) for t in ls]
        print(f"Medelvärdet är {medel_värde(tlist)}")
    except ValueError:
        print("Felaktiga tal:", s)
    except KeyboardInterrupt:
        print("Programmet avslutas")
        exit()

print("Programmet fortsätter ... ")


main()
