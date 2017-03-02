# http://acmp.ru/asp/do/index.asp?main=task&id_problem=748

import sys
a = []
X = 4
Y = 4
cute = True

i = 0
while i < Y:
    a.append([str(s) for s in sys.stdin.readline().strip().split()])
    i += 1
# print (a)


y = 0
while y < Y - 1:
    x = 0
    while x < X - 1:
        if a[y][0][x] == 'W' and a[y][0][x + 1] == 'W' and a[y + 1][0][x] == 'W' and a[y + 1][0][x + 1] == 'W':
            print('No')
            cute = False
            break
        
        if a[y][0][x] == 'B' and a[y][0][x + 1] == 'B' and a[y + 1][0][x] == 'B' and a[y + 1][0][x + 1] == 'B':
            print('No')
            cute = False
            break        

        x += 1
    y += 1


if cute == True:
    print ('Yes')
