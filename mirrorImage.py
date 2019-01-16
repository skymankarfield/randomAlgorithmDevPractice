#mirrorImage

stack = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", \
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", \
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", \
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"] 

flippedstack = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", \
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", \
        "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", \
        "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"] 

def solution(image, hrender, mirror=True):
    counter=0
    strconcat=""
    finalconcat=""
    while(len(image)>0):
        if(mirror):
            strconcat=strconcat+image.pop()
        else:
            strconcat=strconcat+image.pop(0)
        counter+=1
        if(counter==hrender or len(image)==0):
            if(mirror):
                finalconcat=strconcat+"\n"+finalconcat
            else:
                finalconcat=finalconcat+"\n"+strconcat
            strconcat=""
            counter=0
    print(finalconcat)
    
print("===Original image===")
solution(stack,10,mirror=False)
print("\n===Flipped image===\n")
solution(flippedstack,10)
