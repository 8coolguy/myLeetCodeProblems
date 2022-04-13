class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #my solution worked but not the right way the second way works in right runtime by usind dp
        #calls dp[i] =max
        #dp=[]
        #for i in range(len(nums)):
        #    dp.append(nums[i])
        #    for j in range(i+2,len(nums)+1):
        #        dp.append(dp[-1]+nums[i:j][-1])
        #print(dp)
        #return max(dp)
        dp=[0]*len(nums)
        for i,num in enumerate(nums):
            dp[i]=max(dp[i-1]+num,num)
        return max(dp)
