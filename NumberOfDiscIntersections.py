#NumberOfDiscIntersections

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    circles = list()
    current_center = 0
    final_result = 0
    for circle in A:
        #print(str(circle))
        for circle1 in circles:
            #print("circle1("+str(current_center-circle)+","+str(current_center+circle)+")")
            #print("circle2("+str(circle1[0])+","+str(circle1[1])+")")
            if (((current_center-circle) >= circle1[0] and (current_center-circle) <= circle1[1]) or((current_center+circle) >= circle1[0] and (current_center+circle) <= circle1[1]) or
                (circle1[0] >= (current_center-circle) and circle1[0] <= (current_center+circle)) or (circle1[1] >= (current_center-circle) and (circle1[1] <= current_center+circle))):
                if (final_result > 10000000):
                    return -1
                final_result = final_result + 1
                #print("Intersect!")
        circles.append(([(current_center-circle),(current_center+circle)]))
        current_center = current_center + 1
    #print(str(circles))
    return final_result
