# acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=726

import sys

N, = [int(s) for s in sys.stdin.readline().strip().split()]
lst = [int(s) for s in sys.stdin.readline().strip().split()]

# [12, 7, 92, 5, 18, 4, 32, 48, 11, 74]



i_now = 0


while i_now < N - 1:
    i_next = i_now + 1
    i_min = i_now

    while i_next < N:
        if lst[i_min] > lst[i_next]:
            i_min = i_next
        i_next += 1

    lst[i_min], lst[i_now] = lst[i_now], lst[i_min]

    i_now += 1

#print (i_now)
#print (i_min)


# меняем с 0, меняем с 1, меняем с 2, .., меняем с n - 2

#print (lst) 

p = 0
while p < N:
    lst[p] = str(lst[p])
    p += 1


print (' '.join(lst))
