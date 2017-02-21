# acmp.ru/index.asp?main=task&id_task=2

import sys
n, = [int(s) for s in sys.stdin.readline().strip().split()]
p = 0
 
if n == 0:
    print (1)
if n > 0:
    for i in range(1,n+1):
        p = p + i
    print (p)
if n < 0:
    for i in range(1,-(n-1)):
        p = p + i
    print (-(p - 1))
