# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    sumElem = 0
    # remove initial '1's
    initial_ones = 0
    limit = len(A)
    while A[initial_ones] == 1:
        initial_ones += 1
        if initial_ones >= limit:
            return 0
    del A[0:initial_ones]
    for i in range(len(A)):
        sumElem += A[i]
    last_zero = -1
    passed = 0
    remaining_sum = sumElem
    for i in range(len(A)):
        if A[i] == 0:
            ones_between = i - last_zero - 1
            remaining_sum -= ones_between
            last_zero = i
            passed += remaining_sum
            if passed > 1000000000:
                return -1
    return passed
