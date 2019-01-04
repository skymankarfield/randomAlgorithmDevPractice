#BinaryGap

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def dec_to_bin(x):
    return int(bin(x)[2:])

def solution(N):
    # write your code in Python 3.6
    if(N<0):
        return 0
    bin_num = dec_to_bin(N)
    str_bin_num = str(bin_num)
    import re
    splitted_bin_num = re.split("1",str_bin_num)
    biggest_gap = 0
    counter = 0
    for splitted_str in splitted_bin_num:
        if(len(splitted_str) > biggest_gap and counter+1<len(splitted_bin_num)):
            biggest_gap = len(splitted_str)
        counter = counter + 1
    return biggest_gap
