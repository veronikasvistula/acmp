# acmp.ru/asp/do/index.asp?main=task&id_course=1&id_section=7&id_topic=118&id_problem=730

import sys

N, = [int(s) for s in sys.stdin.readline().strip().split()]
lst = [int(s) for s in sys.stdin.readline().strip().split()]


# lst = [23, 43, 0, 133, 4, 10]


i = 0

while i < N:
    i_now = N - 1

    while i_now > i:
        i_before = i_now - 1

        if lst[i_before] > lst[i_now]:
            lst[i_now], lst[i_before] = lst[i_before], lst[i_now]
        i_now -= 1
    i += 1

# print(lst)
#    [0, 4, 10, 23, 43, 133]




i_middle = len(lst) // 2


sum_CR = 0
i_CR = 0
while i_CR < i_middle:
    sum_CR += lst[i_CR]
    i_CR += 1

sum_SH = 0
i_SH = N - 1
while i_SH >= i_middle:
    sum_SH += lst[i_SH]
    i_SH -= 1


print (sum_SH - sum_CR)
    








