from math import sqrt

def func(a, b, c):
    root1 = -b/(2*a) + sqrt(b**2-4*a*c)/(2*a)
    root2 = -b/(2*a) - sqrt(b**2-4*a*c)/(2*a)
    return root1, root2

