# acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=10&id_topic=3&id_problem=12

import sys

N, = [int(s) for s in sys.stdin.readline().strip().split()]
arb = [int(s) for s in sys.stdin.readline().strip().split()]

x = 0
arb_max = 0
arb_min = 40000

while x < N:
    if arb[x] > arb_max:
        arb_max = arb[x]
    if arb[x] < arb_min:
        arb_min = arb[x]
    x += 1


print (arb_min, arb_max)
