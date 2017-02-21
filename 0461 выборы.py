import sys

N, = [int(s) for s in sys.stdin.readline().strip().split()]
lst = [int(s) for s in sys.stdin.readline().strip().split()]

p_ZA = N // 2 + 1


i = 0

while i < N:
    i_now = N - 1

    while i_now > i:
        i_before = i_now - 1

        if lst[i_before] > lst[i_now]:
            lst[i_now], lst[i_before] = lst[i_before], lst[i_now]
        i_now -= 1
    i += 1



j = 0
need_ZA = 0

while j < p_ZA:
    need_ZA += lst[j] // 2 + 1
    j += 1

print (need_ZA)

