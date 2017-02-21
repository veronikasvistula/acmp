import sys

zero, = [str(s) for s in sys.stdin.readline().strip().split()]

zero_max = 0
zero_now = 0
x = 0

while x < len(zero):
    if zero[x] == '0':
        zero_now += 1 
        if zero_max < zero_now:
            zero_max = zero_now
        
    if zero[x] == '1':
        if zero_max < zero_now:
            zero_max = zero_now
        zero_now = 0
    x += 1
        
print (zero_max)
