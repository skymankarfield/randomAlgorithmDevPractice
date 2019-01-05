#EquiLeader

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    from collections import Counter
    counter=0
    final_result = []
    for element in A:
        arr1 = A[0:counter+1]
        arr2 = A[counter+1:]
        cnt1 = Counter(arr1)
        cnt2 = Counter(arr2)
        counter = counter + 1
        #print("cnt1="+str(cnt1))
        #print("cnt2="+str(cnt2))
        mstcommon1 = cnt1.most_common(1)
        mstcommon2 = cnt2.most_common(1)
        #print("mstcommon1="+str(mstcommon1))
        #print("array1="+str(arr1))
        #print("mstcommon2="+str(mstcommon2))
        #print("array2="+str(arr2))
        if (len(mstcommon1) > 0 and len(mstcommon2) > 0):
            if mstcommon1[0][1] > (len(arr1)/2) and mstcommon2[0][1]> (len(arr2)/2):
                if mstcommon1[0][0] == mstcommon2[0][0]:
                    #print("adding most common="+str(mstcommon1))
                    final_result.append(mstcommon1[0][0])
    finalcnt = Counter(final_result)
    #print("final counter="+str(finalcnt))
    finalcommon = finalcnt.most_common(1)
    if len(finalcommon) > 0:
        return finalcommon[0][1]
    return 0
    
