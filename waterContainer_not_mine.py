#not my solution
class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        #tracks the highest amt of water so far 
        water = 0
        #looks like binarsy searc
        #2 pointers method
        while i < j:
            #water is the max between the distances and heights and move pointers accordongly`
            water = max(water, (j - i) * min(height[i], height[j]))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return water
