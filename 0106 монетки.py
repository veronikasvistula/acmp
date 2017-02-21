import sys

N, = [int(s) for s in sys.stdin.readline().strip().split()]


lst = []

i = 1
while i <= N:
    lst.append([int(s) for s in sys.stdin.readline().strip().split()])
    i += 1


coin_1 = 0
coin_0 = 0

for coin in lst:
    if coin == [0]:
        coin_0 += 1
    if coin == [1]:
        coin_1 += 1


if coin_0 <= coin_1:
    print (coin_0)
else:
    print (coin_1)
