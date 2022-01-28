#understood after watching nick whites videop
class Solution:
    def rob(self, nums: List[int]) -> int:
        #this is wrong because the valus can be at either ends
        # i can change this so that instead of just even and odds it takes 1 - n-1
        #even_sum =0
        #odd_sum =0
        dp =[0 for _ in range(len(nums)+1)]
        dp[0]=0
        dp[1] =nums[0]
        
        if (len(nums)==0):
            return 0
        elif(len(nums)==1):
            return nums[0]
        
        for i in range(1,len(nums)):
            dp[i+1]=max(dp[i],dp[i-1]+nums[i])
        return dp[len(nums)]
