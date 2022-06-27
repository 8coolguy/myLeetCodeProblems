#back to python I guess for now les go 
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def euc(point):
            return (point[0]**2+point[1]**2)**.5
        res=[]
        for i,point in enumerate(points):
            res.append([euc(point),i])
        res.sort()
        arr=[]
        for i in res[:k]:
            arr.append(points[i[-1]])
        return arr
            
        