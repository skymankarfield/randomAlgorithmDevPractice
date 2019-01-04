#OddOccurrencesInArray

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    import re
    element_array = 0
    string_array = "".join(str(A))
    #print(string_array)
    odd_number = 0
    
    for number in sorted(A):
        ocurrence_array = re.findall(str(number), string_array)
        #print(str(ocurrence_array))
        if (len(ocurrence_array) % 2 != 0):
            odd_number = ocurrence_array.pop()
            return int(odd_number)
