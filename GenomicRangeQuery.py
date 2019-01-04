#GenomicRangeQuery

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def mapLetterToInt(letter):
    if letter == 'A':
        return 1
    elif letter == 'C':
        return 2
    elif letter == 'G':
        return 3
    else:
        return 4

def solution(S, P, Q):
    # write your code in Python 3.6
    S_array = list(S)
    result_array = list()
    counter = 0
    for left_limit in P:
        result_array.append(mapLetterToInt(min(S_array[left_limit:Q[counter]+1])))
        counter = counter + 1
    #print(str(result_array))
    return result_array
