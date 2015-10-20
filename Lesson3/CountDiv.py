# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
from math import floor

def solution(A, B, K):
    # write your code in Python 2.7
    if A % K == 0:
        divisible = floor(float(B - A) / K) + 1
        return int(divisible)
    else:
        lower = A + K - (A % K)
        if lower > B:
            return 0
        divisible = floor(float(B - lower) / K) + 1
        return int(divisible)
