import math

def revInt(n: int):
    if type(n) == int:
        n = str(n)
    return int(n[::-1])
    #return int(s)


num = input("enter number: ")
if int(num) >= 0:
    print(revInt(num))
else:
    num = abs(int(num))
    print(f"-{revInt(num)}")

