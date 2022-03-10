#this solution works and i made it but i think the run tme is pretty slow
class Solution:
    dirs=[[0,1],[0,-1],[1,0],[-1,0]]
    def dfs(self,i,j,visited,matrix,m,n,poa,path):
        if (i,j) in visited:
            return True
        if (i,j) in path:
            return False
        else:
            path.append((i,j))
        if (i==0 or j==0) and poa:
            return True
        if (i==m-1 or j==n-1) and not poa:
            return True
        
        for di in self.dirs:
            x,y =i+di[0] ,j+di[-1]
            #this loop needs to test every direction to find if it reaches an ocean
            #it needs to return false if it nevers an ocean
            if x==-1 or x==m or y==-1 or y==n:
                continue
            if matrix[i][j] < matrix[x][y]:
                continue
            if poa:
                if (x==0 or y==0):
                    return True
            if not poa:
                if (x==m-1 or y==n-1):
                    return True
            
            
            if self.dfs(x,y,visited,matrix,m,n,poa,path):
                return True
        return False 
            
                
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if heights ==[]:
            return None
        
        a_reach=set()
        p_reach=set()
        m=len(heights)
        n=len(heights[0])
        
        r,c = len(heights),len(heights[0])
    
        
    
        
        #we have to go through the matrix and see if every one is able to got to the pac or the atlantic then compare the sets and find the ones that are from both
        
        for i in range(r):
            for j in range(c):
                if self.dfs(i,j,p_reach,heights,r,c,True,[]):
                    p_reach.add((i,j))
                if self.dfs(i,j,a_reach,heights,r,c,False,[]):
                    a_reach.add((i,j))
                    
        res=[]
        for i in a_reach:
            for j in p_reach:
                if i==j:
                    res.append(i)
        return res
