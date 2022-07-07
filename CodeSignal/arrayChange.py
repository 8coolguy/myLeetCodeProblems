def solution(inputArray):
    c=0
    for i in range(1,len(inputArray)):
        if inputArray[i] <= inputArray[i-1]:
            tmp=inputArray[i]        
            inputArray[i]=inputArray[i-1]+1
            c+=inputArray[i]-tmp
    return c

