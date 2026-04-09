import math

def revInt(n: int):
    f = 0
    newN = 0
    if n < 0:
        newN = abs(n)
        f = 1
    else:
        newN = n
    if type(newN) == int:
        s = str(newN)
    reverse_s = s[::-1]
    return reverse_s


num = input("enter number: ")
print(revInt(num))
