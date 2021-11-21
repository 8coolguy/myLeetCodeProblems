class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0 or (x%10 ==0 and x!=0)):
            return False
        #y=str(x)
        #string implementation of it
        #for i in range(len(y)):
        #    if(y[i]!=y[-1-i]):
        #        return False
        #return True
        #nuber implementation //same logic but now instead of using str i use % and divide
        #y =[]

        #while(x!=0):
        #    y.append(x%10)
        #    x=int(x/10)
        #for i in range(len(y)):
        #    if(y[i] != y[-1-i]):
        #        return False
        #return True
        
        y=0
        while(y<x):
            y=y*10+x%10
            x=int(x/10)
        if(x==y or x ==int(y/10)):
            return True
        else:
            return False
        
            
