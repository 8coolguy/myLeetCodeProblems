class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
     #i had the same loginc but my solution never worked  
        if not grid:
            return 0
        res=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=='1':
                    self.dfs(grid,i,j)
                    res+=1
        return res
            
        
    def dfs(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j]="#"
        self.dfs(grid,i+1,j)
        self.dfs(grid,i,j+1)
        self.dfs(grid,i-1,j)
        self.dfs(grid,i,j-1)
            
            