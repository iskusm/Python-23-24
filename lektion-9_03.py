list1 = [4,23,18,11,3,8,9]

n = len(list1)

for i in range(n-1,-1,-1):
    print(list1[i])


print(list1[::-1])

summan = sum(list1)  # beräknar summan av lista

print(summan)

list1.sort()  #storlekordning

print(list1)
