# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

def solution(X, A):
    positions = []
    counter = 0
    index = -1
    for i in range(0, X):
        positions.append(False)
    for leaf in A:
        index += 1
        if positions[leaf - 1] == False
            positions[leaf - 1] = True
            counter += 1
            if counter == X:
                break
    if counter == X:
        return index
    else:
        return -1
            
