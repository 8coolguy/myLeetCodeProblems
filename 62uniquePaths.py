#cmon get these meds no problem
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #m rows 
        #n cols
        dp=[[0 for _ in range(n)] for i in range(m)]
        dp[0][0]=1
        for r in range(m):
            for c in range(n):
                if r ==0 and c==0:
                    continue
                else:
                    if r!=0:
                        dp[r][c]+=dp[r-1][c]
                    if c!=0:
                        dp[r][c]+=dp[r][c-1]
        #print(dp)
        return dp[-1][-1]
                        
        
        
        
        