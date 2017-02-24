# acmp.ru/index.asp?main=task&id_task=41

import sys
N, = [int(s) for s in sys.stdin.readline().strip().split()]
lst = [int(s) for s in sys.stdin.readline().strip().split()]

lst_i = [num for num in range(-100, 101)]
lst_count = [0]*201

i = 0
while i < len(lst):
    
    lst_count[lst[i] + 100] += 1
    i += 1

# print (lst_count)


lst_sort = []
i = 0
while i < len(lst_count):
    if lst_count[i] != 0:
        p = 1
        while p <= lst_count[i]:                        
            lst_sort.append(lst_i[i])
            p += 1
    i += 1



p = 0
while p < len(lst_sort):
    lst_sort[p] = str(lst_sort[p])
    p += 1
print (' '.join(lst_sort))
