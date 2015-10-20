# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    arr = [False] * N
    for num in A:
        if num > 0 and num <= N:
            arr[num - 1] = True
    for i in range(N):
        if arr[i] == False:
            return i + 1
    return N + 1

