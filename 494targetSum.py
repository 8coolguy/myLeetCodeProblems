class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        return self.dfs(nums, target, 0, 0,{})   
        
    def dfs(self,nums,target,i,cur,m):
        key=(i,cur)
        if key in m:
            return m[key]
        if i==len(nums):
            return 1 if cur ==target else 0
        
        add=self.dfs(nums,target,i+1,cur+nums[i],m)
        sub=self.dfs(nums,target,i+1,cur-nums[i],m)
        m[key]=add+sub
        return m[key]
      