#not my solution but inderstand how it is a greedy solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        area =0
        
        while r>l:
            area=max(area,(r-1)*min(height[l],height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
				
        return area