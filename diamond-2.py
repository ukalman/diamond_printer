import sys

diamond_size = int(input())
diction,reversed_diction = dict(),dict()
c = [(" "*(diamond_size-b), "*"*(2*b+1)) for b in range(diamond_size)]

for i in range(diamond_size):
    diction[i] = c[i]

for k in range(diamond_size-2,-1,-1):
    reversed_diction[k] = c[k]

for j in diction.values():
    print(j[0],j[1])

for x in reversed_diction.values():
    print(x[0],x[1])


