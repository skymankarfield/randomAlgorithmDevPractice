#Brackets

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    stack = []
    for x in S:
        if x in ['(', '{', '[']:
            stack.append(x)
        elif x in [')', '}', ']']:
            if len(stack) == 0:
                return 0
            y = stack.pop()
            if x == ')' and y != '(':
                return 0
            elif x == ']' and y != '[':
                return 0
            elif x == '}' and y != '{':
                return 0
    if len(stack) != 0:
        return 0
    return 1
