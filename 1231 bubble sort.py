# http://acmp.ru/asp/do/index.asp?main=task&id_course=2&id_section=12&id_topic=8&id_problem=740

import sys

N, = [int(s) for s in sys.stdin.readline().strip().split()]
lst = [int(s) for s in sys.stdin.readline().strip().split()]


# lst = [23, 43, 0, 133, 4]


bub_step = 0
i = 0

while i < N:
    i_now = N - 1

    while i_now > i:

        i_before = i_now - 1

        if lst[i_before] > lst[i_now]:
            lst[i_now], lst[i_before] = lst[i_before], lst[i_now]
            bub_step += 1
        i_now -= 1
    i += 1

#print(lst)
print(bub_step)


    
# с конца до 0, с конца до 1, с конца до 2, с конца до 3, .. 
