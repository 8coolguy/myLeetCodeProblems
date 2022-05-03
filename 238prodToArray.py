#not my soltuoin but  ithinkn i get it
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
       
        n = len(nums)
        
        cura = nums[0]
        curb = nums[n-1]
                
        a = [1] * n
        #switch the pointers every iteration
        for i in range(1,n):
            a[i] *= cura
            a[-1-i] *= curb
            cura *= nums[i]
            curb *= nums[n-1-i]

        return a
