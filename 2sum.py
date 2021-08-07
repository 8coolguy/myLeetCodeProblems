

#solution works
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ans =[-1,-1]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if ((i!= j) and (nums[i]+nums[j] ==target)): 
                    ans[0]=i
                    ans[1]=j
                    return ans
         
