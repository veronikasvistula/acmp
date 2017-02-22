# acmp.ru/asp/do/index.asp?main=task&id_problem=16

import sys
 
N, = [int(s) for s in sys.stdin.readline().strip().split()]
lst = [int(s) for s in sys.stdin.readline().strip().split()]

tsl = []
for i in range(N - 1, -1, -1):
    tsl.append(lst[i])

p = 0
while p < N:
    tsl[p] = str(tsl[p])
    p += 1


print (' '.join(tsl))
