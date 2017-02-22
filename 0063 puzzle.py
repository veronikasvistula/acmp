# acmp.ru/asp/do/index.asp?main=task&id_problem=14

import sys

S, P = [int(s) for s in sys.stdin.readline().strip().split()]

i = 0
while i <= S // 2:
    a = S - i
    if a * i == P:

        print (i, a)
        break
    i += 1
