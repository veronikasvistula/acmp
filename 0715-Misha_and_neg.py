# acmp.ru/asp/do/index.asp?main=task&id_problem=749

import sys

Y, X = [int(s) for s in sys.stdin.readline().strip().split()]
poz = []
neg_wrong = []
mist = 0

i = 0
while i < Y:
    poz.append([str(s) for s in sys.stdin.readline().strip().split()])
    i += 1
nothing = [str(s) for s in sys.stdin.readline().strip().split()]
i = 0
while i < Y:
    neg_wrong.append([str(s) for s in sys.stdin.readline().strip().split()])
    i += 1

y = 0
while y < Y:
    x = 0
    while x < X:
        if poz[y][0][x] == neg_wrong[y][0][x]:
            mist += 1

        x += 1
    y += 1


print (mist)

