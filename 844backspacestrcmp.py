class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        #alot of times with strings you use stacks
        
        #first solution uses stacks and stores them 
        s1=[]
        s2=[]
        res=False
        for i in s:
            if i!="#":
                s1.append(i)
            elif(len(s1)!= 0):
                s1.pop()
        for i in t:
            if i!="#":
                s2.append(i)
            elif len(s2)!= 0:
                s2.pop()
        if(str(s1)==str(s2)):
            res= True
        else:
            res= False
            
        return res
        # i want to do this again using pointers and no memory
            
            
        
        

