# acmp.ru/asp/do/index.asp?main=task&id_problem=705

import sys
N, = [int(s) for s in sys.stdin.readline().strip().split()]
lst = [int(s) for s in sys.stdin.readline().strip().split()]
i_lst = []
money = 0

for num in range(1, N + 1):
    i_lst.append(num)

i_now = 0
while i_now < N - 1:
    i_next = i_now + 1
    while i_next < N:
        if lst[i_now] < lst[i_next]:
            lst[i_next], lst[i_now] = lst[i_now], lst[i_next]
            i_lst[i_next], i_lst[i_now] = i_lst[i_now], i_lst[i_next]
        i_next += 1
    i_now += 1


i = 0
i_lst_0 = 0
while i < len(i_lst):
    if i_lst [i] > i_lst_0:
        money += lst[i] * (i_lst[i] - i_lst_0)
        i_lst_0 = i_lst[i]
    i += 1


print (money)
