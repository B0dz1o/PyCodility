# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N, A):
    # write your code in Python 2.7
    counters = []
    for i in range(N):
        counters.append(0)
    N_cmp = N + 1
    max_counter = 0
    for operation in A:
        if operation == N_cmp:
            for i in range(N):
                counters[i] = max_counter
        else:
            counters[operation-1] += 1
            if counters[operation-1] > max_counter:
                max_counter = counters[operation-1]
            
    return counters
            
