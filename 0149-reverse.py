# acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=10&id_topic=4&id_problem=16

import sys
 
N, = [int(s) for s in sys.stdin.readline().strip().split()]
lst = [int(s) for s in sys.stdin.readline().strip().split()]

middle = N // 2

i_start = 0
i_finish = N - 1
while i_start < middle:
    lst[i_start], lst[i_finish] = lst[i_finish], lst[i_start]
    i_start += 1
    i_finish -= 1

p = 0
while p < N:
    lst[p] = str(lst[p])
    p += 1


print (' '.join(lst))
