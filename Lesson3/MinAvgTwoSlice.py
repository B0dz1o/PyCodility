# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(A):
    # write your code in Python 2.7
    pref_sums = prefix_sums(A)
    min_index = 0
    min_avg = 1.0 / 2 * (A[0] + A[1])
    for i in xrange(0, len(A) - 1):
        for length in xrange(2, len(A) + 1 - i):
            avg = float(count_total(pref_sums, i, i + length - 1))
            if avg / length < min_avg:
                min_avg = avg / length
                min_index = i
            print avg / length, '\t', i
    return min_index        
    
def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in xrange(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P
    
def count_total(P, x, y):
    return P[y + 1] - P[x]
    
#print solution([4, 2, 2, 5, 1, 5, 8])
#print solution([1,2,3])
#print solution([1,2,1])
print solution([-3, -5, -8, -4, -10])
