# http://acmp.ru/index.asp?main=task&id_task=120

import sys
Ly, Lx = [int(s) for s in sys.stdin.readline().strip().split()]

b = []
y = 0
while y < Ly:
    s = [int(s) for s in sys.stdin.readline().strip().split()]
    b.append(s)
    y += 1

x = Lx - 2
while x >= 0:
    b[Ly-1][x] += b[Ly-1][x+1]
    x -= 1

y = Ly - 2
while y >= 0:
    b[y][Lx-1] += b[y+1][Lx-1]
    y -= 1


#======

y = Ly-1
while y > 0:
    x = Lx - 1
    while x > 0:
        if b[y][x-1] <= b[y-1][x]:
            b[y-1][x-1] += b[y][x-1]
        if b[y][x-1] > b[y-1][x]:
            b[y-1][x-1] += b[y-1][x]
        x -= 1
    y -= 1




print(b[0][0])
    
