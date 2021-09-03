#no idea how this works ngl
#no work https://www.youtube.com/watch?v=9d636Y8qfLw
class Solution:
    #if one of the coordinates is on the limit it should be added
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        valsX=trees.copy()
        valsY=trees.copy()
        vals =trees.copy()
        n =len(trees)
        ans=[]

        for i in range(n):
            vals[i]=trees[i][0]+trees[i][-1]
            valsX[i]=trees[i][0]
            valsY[i]=trees[i][-1]
        
        smallPost=min(vals)
        bigPost =max(vals)
        sx=min(valsX)
        bx=max(valsX)
        sy=min(valsY)
        by=max(valsY)
        for i in range(n):
            if smallPost == vals[i] or bigPost ==vals[i] or sx ==valsX[i] or bx ==valsX[i] or sy ==valsY[i] or by ==valsY[i]:
                ans.append(trees[i].copy())
        return ans

