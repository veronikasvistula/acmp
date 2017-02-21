# acmp.ru/index.asp?main=task&id_task=174

import sys

N, = [int(s) for s in sys.stdin.readline().strip().split()]
love_money = [float(s) for s in sys.stdin.readline().strip().split()]
money_G, = [float(s) for s in sys.stdin.readline().strip().split()]

i = 0
while i < N:
    i_now = N - 1

    while i_now > i:
        i_before = i_now - 1

        if love_money[i_before] > love_money[i_now]:
            love_money[i_now], love_money[i_before] = love_money[i_before], love_money[i_now]
        i_now -= 1
    i += 1



#print (love_money)


j = 0
while j < N:
    if money_G < love_money[j]:
        money_G = (money_G + love_money[j]) / 2
    j += 1



print ("%.6f" % (money_G))

