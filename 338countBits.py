#ok so my solution was O(n32) while the other solution was just a flat(o(n)) with the smae space
class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[0]*(n+1)
        
        # (i & (i -1)) is actually Brian Kernighan’s Algorithm, so always keep it handy for counting ones
        for i in range(1 ,n+1):
            res[i] = res[i & (i-1)] + 1
        #for i in range(n+1):
            #count=0
            #for j in range(32):
                #if (i >>j) & 1:
                    #count+=1
            #res.append(count)
        return res
                    
            
        
