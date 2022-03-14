#got this one on my own with dfs search streak 1
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        dirs=[[1,0],[-1,0],[0,1],[0,-1]]
        
        original_color=image[sr][sc]
        image[sr][sc]=newColor
        r=len(image)
        c=len(image[0])
        visited=set()
        def dfs(i,j,visited,image,m,n,directions,orC):
            if (i,j) in visited:
                return
            visited.add((i,j))
            for di in dirs:
                x,y=i+di[0],j+di[-1]
                if x>=0 and x<m and y>=0 and y<n:
                    if image[x][y]==orC:
                        image[x][y]=newColor
                        dfs(x,y,visited,image,m,n,dirs,orC)
            return
        dfs(sr,sc,visited,image,r,c,dirs,original_color)
        return image