# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(N, A):
    # write your code in Python 2.7
    counters = []
    for i in range(N):
        counters.append(0)
    N_cmp = N + 1
    max_counter = 0
    last_max = 0
    for operation in A:
        if operation == N_cmp:
            last_max = max_counter
        else:
            op_num = operation - 1
            if counters[op_num] < last_max:
                counters[op_num] = last_max + 1
            else:
                counters[op_num] += 1
            if counters[op_num] > max_counter:
                max_counter = counters[op_num]
    for i in range(N):
        if counters[i] < last_max:
            counters[i] = last_max
        
            
    return counters
            
