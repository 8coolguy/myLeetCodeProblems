#ez on my own
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res =[]
        if numRows ==0:
            return res
        res.append([1])
        for i in range(2,numRows+1):
            tmp=[0]*i
            for j in range(i):
                if j ==0 or j==i-1:
                    tmp[j]=1
                else:
                    tmp[j]=res[i-2][j]+res[i-2][j-1]
            res.append(tmp)
        return res
        
                    
                
                
        