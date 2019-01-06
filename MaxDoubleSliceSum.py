#MaxDoubleSliceSum

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    max_ending = max_slice = 0
    positions = []
    counter = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
        if max_ending == 0 or max_ending < max_slice: 
            positions.append(counter)
            #print("positions.append("+str(counter)+")")
            #print("max_ending="+str(max_ending))
            #print("max_slice="+str(max_slice))
        counter = counter + 1
    #print("positions="+str(positions))
    
    counter = 1
    sum = 0
    sum_array = []
    for a in A[1:]:
        if counter in positions:
           sum_array.append(sum)
           sum = 0
        else:
            #print("Enters to position="+str(counter))
            sum = sum + a
            if counter == len(A)-1:
                sum_array.append(sum)
        counter = counter + 1
    
    sum_array.sort(reverse=True)
    
    return sum_array[0]+sum_array[1]
