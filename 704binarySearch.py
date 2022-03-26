#not sure how I didn't do this already
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums ==None:
            return None
        
        lo=0
        hi=len(nums)-1
        
        while(hi>=lo):
            mid= (hi+lo)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target:
                hi =mid-1
            elif nums[mid] < target:
                lo=mid+1
        return -1
        