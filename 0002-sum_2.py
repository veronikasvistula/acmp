# acmp.ru/index.asp?main=task&id_task=2

import sys
n, = [int(s) for s in sys.stdin.readline().strip().split()]
p = 0

if n == 0:
    print (1)

if n > 0:
    i = 1
    while i <= n:
        p += i
        i += 1
    print (p)

if n < 0:
    i = 1
    while i >= n:
        p += i
        i -= 1
    print (p)
