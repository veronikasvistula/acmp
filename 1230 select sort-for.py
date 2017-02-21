# acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=726

import sys
N, = [int(s) for s in sys.stdin.readline().strip().split()]
lst = [int(s) for s in sys.stdin.readline().strip().split()]


for i in range(N):
    minmin = 0
    for j in range(i, N):
        if (lst[i] > lst[j]):
            
            lst[i], lst[j] = lst[j], lst[i]

p = 0
while p < len(lst):
    lst[p] = str(lst[p])
    p += 1
    
print (' '.join(lst))
