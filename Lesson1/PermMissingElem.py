# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def sum_one_to_N(N):
    sum = (1 + N) * N / 2
    return sum

def solution(A):
    full_sum = sum_one_to_N(len(A) + 1)
    sum_A = 0
    for i in A:
        sum_A += i
    return full_sum - sum_A
