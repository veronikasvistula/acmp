import sys

L, = [int(s) for s in sys.stdin.readline().strip().split()]
k = [int(s) for s in sys.stdin.readline().strip().split()]

k_max = 0 

i = 0


while i < L:
    k_all = k[i % L] + k[(i + 1) % L] + k[(i + 2) % L]
    
    if k_max < k_all:
        k_max = k_all
    
    i += 1

print (k_max)
