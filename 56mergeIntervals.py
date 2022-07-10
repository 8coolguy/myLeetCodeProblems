#another one in the books august I go crazy on the leet code prepping for the interviews
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        n=len(intervals)
        res=[]
        rmv =[]
        for i in range(n):
            if i in rmv:
                continue
            cur=intervals[i]
            
            for j in range(i+1,n):
                merge=intervals[j]
                if merge[0] <= cur[1]:
                    cur[-1]=max(cur[-1],merge[-1])
                    rmv.append(j)
            res.append(cur)
        return res