# got it but I want to do it again using the graph logic
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        arr=[0]*n
        _arr=[0]*n
        for i in trust:
            arr[i[0]-1]+=1
            _arr[i[-1]-1]+=1
        count=0
        res=-1
        for i in range(len(arr)):
            if arr[i]==0 and _arr[i]==n-1:
                res=i+1
                count+=1
            
        if count==1:
            return res
        return -1