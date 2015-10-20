# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    sum = 0
    for i in A:
        sum += i
    cur_val = - sum
    min_val = abs(2 * A[0] - sum)
    for i in A:
        cur_val += 2 * i
        if abs(cur_val) < min_val:
            min_val = abs(cur_val)
    return min_val

