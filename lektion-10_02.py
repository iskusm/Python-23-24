while True:
    n = int(input("n? "))
    if n < 0:
        print("Det måste vara ett positivt tal.")
        break
    summa = 0
    k = 1
    while k <= n:
        summa = summa + k
        k = k + 1
    print(f"Summan blir {summa}")
