påsar = 3
äpplen_i_påse = 12

print(f"Det finns totalt {påsar * äpplen_i_påse} äpplen.")

val = 356 / 7

print("Python f-sträng för flyttal")
print(f"{val}")

print(f"{val:.5f}")

procent = 1 / 7.0
print("Python f-sträng för procent")
print(f"{procent}")

print(f"{procent:.2%}")

print("Python f-sträng för ordnat formatering")

for x in range(1, 11):
    print(f"{x:2} {x*x:3} {x*x*x:4}")
