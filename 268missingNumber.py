# i came up with the summing solution on my own and the bit one I had to read upon why it worked
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n =len(nums)
        #tot=0
        for i in range(len(nums)):
            n^=i
            n^=nums[i]
        #    tot+=i+1
        #    tot-=nums[i]
        
        
        #bit manipulation version
        return n
            
