# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    counter_arr = []
    len_A = len(A)
    for i in A:
        if i > len_A:
            return 0
        counter_arr.append(0)
    for i in A:
        counter_arr[i-1] += 1
        if counter_arr[i-1] == 2:
            return 0
    return 1

