#OddOccurrencesInArray

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    from collections import Counter
    counter = Counter(A)
    for key, value in counter.items():
        if (value % 2 != 0):
            return int(key)
            
