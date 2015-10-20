# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    N = len(A)
    A.append(0)
    for counter in range(N):
        num = A[counter]
        while num >= 0 and num <= N and num != A[num]:
            temp = A[num]
            A[num] = num
            num = temp
    
    for counter in range(1,N + 1):
        if A[counter] != counter:
            return counter
    return N


