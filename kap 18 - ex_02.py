import os

if os.path.exists("C://Users//iskusm//Documents//favoritfilmer.txt"):
    f = open("C://Users//iskusm//Documents//favoritfilmer.txt", "r")

    x = f.read()
    f.close()
    print(x)
else:
    print("Det finns inte filen.")
    

