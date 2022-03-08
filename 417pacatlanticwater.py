#still working on this for now come back to it tommorrow on 03/08
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if heights ==[]:
            return None
        
        a_reach=set()
        p_reach=set()
        
        r,c = len(heights),len(heights[0])
        self.dirs=[[0,1],[0,-1],[1,0],[-1,0]]
        
        def dfs(i,j,visited,matrix,m,n):
            for di in dirs:
                x,y =
                if x < 0 or x >= m or y < 0 or y >= n:
                    continue
