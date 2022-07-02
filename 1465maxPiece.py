#after 200  imma start doing hards every other day
class Solution:
        def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
            horizontalCuts.append(0)
            horizontalCuts.append(h)

            verticalCuts.append(0)
            verticalCuts.append(w)

            verticalCuts.sort()
            horizontalCuts.sort()
            print(verticalCuts)
            print(horizontalCuts)
            max_h=0
            for i in range(len(horizontalCuts)-1):
                if horizontalCuts[i+1]-horizontalCuts[i]>max_h:
                    max_h=horizontalCuts[i+1]-horizontalCuts[i]
            max_v=0
            for i in range(len(verticalCuts)-1):
                if verticalCuts[i+1]-verticalCuts[i]>max_v:
                    max_v=verticalCuts[i+1]-verticalCuts[i]
            return max_v*max_h %(10**9+7)
            
        
    
    
    
    
        
        