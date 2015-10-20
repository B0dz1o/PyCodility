# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    if N == 1:
        if A[0] == 1:
            return 2
        else:
            return 1
    A.append(0)
    for i in range(N + 1):
        val = A[i]
        while val >= 0 and val <= N and val != A[val]:
            temp = A[val]
            A[val] = val
            val = temp
            
    for i in range(N + 1):
        if i != A[i] and i != 0:
            return i
    return N + 1
        
