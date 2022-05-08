#pretty straight forward
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        res=[]
        if m*n != len(original):
            return res
        
        for i in range(m):
            res.append([])
            for j in range(n):
                
                res[i].append(original.pop(0))
        return res
        
