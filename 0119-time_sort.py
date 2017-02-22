# acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=728

import sys

N, = [int(s) for s in sys.stdin.readline().strip().split()]
lst = []

i = 1
while i <= N:
    lst.append([int(s) for s in sys.stdin.readline().strip().split()])
    i += 1

# [[10, 20, 30], [7, 30, 0], [23, 59, 59], [13, 30, 30]]

i_now = 0
while i_now < N - 1:
    i_next = i_now + 1
    i_min = i_now

    while i_next < N:
        if lst[i_min][0] > lst[i_next][0]:
            i_min = i_next
        if lst[i_min][0] == lst[i_next][0]:
            if lst[i_min][1] > lst[i_next][1]:
                i_min = i_next
            if lst[i_min][1] == lst[i_next][1]:
                if lst[i_min][2] > lst[i_next][2]:
                    i_min = i_next
        i_next += 1
        
    lst[i_min], lst[i_now] = lst[i_now], lst[i_min]
    
    i_now += 1






    
# [[7, 30, 0], [10, 20, 30], [13, 30, 30], [23, 59, 59]]


p1 = 0
while p1 < len(lst):
    p2 = 0
    while p2 < 3:
        lst[p1][p2] = str(lst[p1][p2])
        p2 += 1
    p1 += 1

    
for lsts in lst:
    print (' '.join(lsts))

