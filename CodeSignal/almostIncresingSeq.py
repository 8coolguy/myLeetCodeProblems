#got it les go boi finally first cs in the repo
def solution(sequence):
    
    n=len(sequence)
    def onlyInc(a):
        for i in range(1,len(a)):
            if a[i-1] >=a[i]:
                return False
        return True
    
    if onlyInc(sequence):
        return True
    for i in range(1,n):
        if sequence[i-1] >=sequence[i]:
            print(i)
            tmp=sequence[:]
            tmp.pop(i-1)
            if onlyInc(tmp):
                return True
            tmp=sequence[:]
            tmp.pop(i)
            if onlyInc(tmp):
                return True
    return False
        
#    removed =False
#    for i in range(len(sequence)-1):
#        if(sequence[i]>=sequence[i+1]):
#            if(removed):
#                return False
#            else:
#                print(i)
#                removed =True
#                if(i==len(sequence)-1 or i==0):
#                    continue
#                elif(sequence[i-1] >sequence[i+1]):
#                    return False
#                
#   return True 
                                                   
                
                
            


