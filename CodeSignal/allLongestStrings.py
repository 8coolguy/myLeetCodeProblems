def solution(inputArray):
    m=0
    i =0
    while i<len(inputArray):
        #print(inputArray[i])
        if len(inputArray[i])>m:
            m=len(inputArray[i])
            i=0
            continue
        elif len(inputArray[i])<m:
            print(inputArray.pop(i))
            i-=1
        i+=1
    return inputArray

