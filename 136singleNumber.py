#2 solutions one for space one for time baby
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #o(2nlogn solution or smhng)
        #o(1)space
        #nums.sort()
        #for i in range(0,len(nums),2):
        #    if i+1 ==len(nums) or nums[i]!=nums[i+1]:
        #        return nums[i]
        
        
        
        
        #o(n/2-1) space 
        #
        s=set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        return list(s)[0]
            
                
