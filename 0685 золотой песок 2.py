import sys
A1, A2, A3, B1, B2, B3 = [int(s) for s in sys.stdin.readline().strip().split()]

A = [A1, A2, A3]
B = [B1, B2, B3]

i_now = 0
while i_now < len(A) - 1:
    i_next = i_now + 1
    while i_next < len(A):
        if A[i_now] > A[i_next]:
            A[i_now], A[i_next] = A[i_next], A[i_now]

        i_next += 1
    i_now += 1



i_now = 0
while i_now < len(B) - 1:
    i_next = i_now + 1
    while i_next < len(B):
        if B[i_now] > B[i_next]:
            B[i_now], B[i_next] = B[i_next], B[i_now]

        i_next += 1
    i_now += 1


sum = 0
for num in range(3):
    sum += A[num] * B[num]

print (sum)
