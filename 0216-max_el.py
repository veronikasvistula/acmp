import sys
N, = [int(s) for s in sys.stdin.readline().strip().split()]
lst = [int(s) for s in sys.stdin.readline().strip().split()]
lst_part = [int(s) for s in sys.stdin.readline().strip().split()]

# 5
# 1 3 5 7 9
# 2 4

max_el = 0
i_el = 0

i = lst_part[0] - 1
j = lst_part[1]

while i < j:
    if lst[i] > max_el:
        max_el = lst[i]
        i_el = i + 1
    i += 1

print (max_el, i_el)
