def solution(inputArray):
    a=inputArray
    res=0
    for i in range(1,len(a)):
        res=max(abs(a[i]-a[i-1]),res)
    return res
        

