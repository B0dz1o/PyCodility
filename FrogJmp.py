# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
import math

def solution(X, Y, D):
    dist = float(Y - X)
    steps = math.ceil(dist / D)
    return int(steps)
