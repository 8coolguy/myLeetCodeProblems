#not finished this rn
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        arr=[0]*n

        for i in trust:
            arr[i[0]-1]+=1
        res=-1
        count=0
        print(arr)
        for i in range(len(arr)):
            if arr[i]!=n-1 and arr[i]!=0:
                return -1
            if arr[i]==0:
                res=i+1
                count+=1

        if count==1:
            return res
        return -1
