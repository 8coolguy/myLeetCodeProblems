#just a simple binary search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if(len(nums)==0):
            return 0
        
        hi= len(nums)-1
        lo =0
        while(hi >= lo):
            mi=int((hi + lo)/2)
            if target==nums[mi]:
                return mi
            elif target >nums[mi]:
                lo =mi+1
            elif target <nums[mi]:
                hi=mi-1
                
        return lo
        
