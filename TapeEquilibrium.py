#TapeEquilibrium

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    first_tape = A[0:len(A)-1]
    second_tape = A[::-1]
    second_tape = second_tape[0:len(second_tape)-1]
    sum_second_tape = sum(second_tape)
    #print(str(first_tape))
    #print(str(second_tape))
    #print(str(sum_second_tape))
    #first_tape_array = []
    #second_tape_array = []
    counter = 0
    final_result = 2000
    counter3 = 0
    for element_array in first_tape:
        counter = counter + element_array
        #print ("counter="+str(counter)+" - sum_second_tape="+str(sum_second_tape))
        result = abs(counter - sum_second_tape)
        #print("Preliminary result="+str(result))
        if (result < final_result):
            final_result = result
        sum_second_tape = sum_second_tape - second_tape[(len(second_tape)-1)-counter3]
        counter3 = counter3 + 1
    return final_result
