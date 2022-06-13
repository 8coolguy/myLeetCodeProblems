
#another dfs problem I want to get good at this over the summer
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        tot=0
        memo = [[-1] * len(triangle) for _ in range(len(triangle))]
        def dfs(i,j):
            if i == len(triangle):
                return 0
            if memo[i][j]!=-1:
                return memo[i][j]
            
            memo[i][j] = triangle[i][j]+min(dfs(i+1,j),dfs(i+1,j+1))
            return memo[i][j]
        return dfs(0,0)
            
            
        