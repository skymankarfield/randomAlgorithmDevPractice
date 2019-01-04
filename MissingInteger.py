#MissingInteger

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    list1 = set(range(1,100000))
    list2 = set(A)

    list3 = list1.intersection(list2)
    
    if len(list3) == 0:
        return 1
    elif (len(list3) == len(list1)):
        return 100001
    elif len(list3) > 0:
        for integer in list1:
            if integer not in list2:
                return integer
