# -*- coding: utf-8 -*-
# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"
#Let len(s) be the length of a slice s, sum(s) the sum of the all elements of the slice s, and ave(s) the average of the slice s. Then for an arbitrary array, every slice s having len(s) > 3 contains a sub-slice s’ such that ave(s) >= ave(s’).

#Proof.

#Suppose that s is a slice having len(s) > 3 and does NOT contain a sub-slice s’ such that ave(s) >= ave(s’). Since len(s) > 3, s can be divided into sub-slices t and u.

#Then,

#ave(t) = sum(t) / len(t), and ave(u) = sum(u) / len(u).

#ave(s) = sum(s) / len(s)
#= [sum(t) + sum(u)] / [len(t) + len(u)]
#= [len(t) * ave(t) + len(u) * ave(u)] / [len(t) + len(u)].

#If ave(u) >= ave(t) then let s’ be t

#ave(s) = [len(t) * ave(t) + len(u) * ave(u)] / [len(t) + len(u)]
#>= [[len(t) + len(u)] * ave(t)] / [len(t) + len(u)]
#= ave(t)
#= ave(s’).

#Otherwise, if ave(t) >= ave(u) then let s’ be u

#ave(s) = [len(t) * ave(t) + len(u) * ave(u)] / [len(t) + len(u)]
#>= [[len(t) + len(u)] * ave(u)] / [len(t) + len(u)]
#= ave(u)
#= ave(s’).

def solution(A):
    # write your code in Python 2.7
    pref_sums = prefix_sums(A)
    min_index = 0
    min_avg = 1.0 / 2 * (A[0] + A[1])
    for i in xrange(0, len(A) - 2):
        avg_two = (A[i] + A[i + 1]) / 2.0
        avg_three = (A[i] + A[i + 1] + A[i + 2]) / 3.0
        if avg_two < min_avg:
            min_avg = avg_two
            min_index = i
        elif avg_three < min_avg:
            min_avg = avg_three
            min_index = i
    # last two
    avg_two = (A[-1] + A[-2]) / 2.0
    if avg_two < min_avg:
            min_avg = avg_two
            min_index = len(A) - 2
    return min_index        
    

