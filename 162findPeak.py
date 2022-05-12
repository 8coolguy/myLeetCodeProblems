#binary serach with different requirments to moven the boundries
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        lo=0
        hi=len(nums)-1
        while hi >=lo:
            mid=(hi+lo)//2
            if (mid-1 < 0 or nums[mid] > nums[mid-1]) and (mid+1 >=len(nums) or nums[mid] >nums[mid+1]):
                return mid
            elif mid-1>=0 and nums[mid]<nums[mid-1]:
                hi=mid-1   
            elif mid+1 <len(nums) and nums[mid]<nums[mid+1]:
                lo=mid+1
            
            
            
        return lo
                
            
            
        
