
#for problems i need to look at the probelm more espically test cases:
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k==0:
            return s
        if k==1:
            s= list(s)
            minQueue=s.copy()
            for _ in s:
                s.append(s.pop(0))
                if id("".join(s)) <id("".join(minQueue)):
                    minQueue =s
                
                
            return "".join(minQueue)
            
            
            
        if k>=2:
            return "".join(sorted(s))
            
            
