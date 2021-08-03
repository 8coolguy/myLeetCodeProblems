class Solution:
    #recursive function counting
    #create a list of flags 
 
    def largestIsland(self, grid: List[List[int]]) -> int:
        def maxI(grid,flags,r,c):
            flags[r][c]=1
            total=0
            #check if its not on a boundry edge 
            #up
            if(r!=0):
                #check if its not already counted
                if(flags[r-1][c]==0 and grid[r-1][c]==1):
                    
                    total+=maxI(grid,flags,r-1,c)
            #left        
            if(c!=0):
                if(0==flags[r][c-1] and grid[r][c-1]==1):
                    total+=maxI(grid,flags,r,c-1)
                    
            #down
            if(r!=len(grid)-1):
                if(flags[r+1][c] ==0and grid[r+1][c]==1):
                    
                    total+=maxI(grid,flags,r+1,c)
                
            #right        
            if(c!=len(grid)-1):
                if(flags[r][c+1]==0 and grid[r][c+1]==1):
                    
                    total+=maxI(grid,flags,r,c+1)

            return total+1
        def maxSize(grid,n):
            
            flags =default_flag=[[0 for c in range(n)] for r in range(n)]
            
            max_size=0
            for i in range(n):
                for j in range(n):
                    temp =maxI(grid,flags,i,j)
                    if ((max_size < temp) and grid[i][j]):
                        max_size=temp
                    flags =[[0 for c in range(n)] for r in range(n)]
                      
            return max_size
        
        
        
        n =len(grid)
        maX= maxSize(grid,n)
        for i in range(n):
            for j in range(n):
                if grid[i][j] ==0:
                    grid[i][j]=1
                    temp =maxSize(grid,n)
                    if maX<temp:
                        maX=temp
                    grid[i][j]=0
        return maX
                        
                   
        
       
                    