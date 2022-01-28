#my solution did not work but i also used a dp array in the same way iwas close but not correct 
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # in the dp array we will go from 0 to target and call on dp to get vals instead of recalcualting
        dp=[0 for _ in range(target+1)]
        nums.sort()
        for i in range(1, target+1):
            for j in nums:
                if(j >i):
                    break
                if(j == i):
                    dp[i]+=1
                if (j < i):
                    dp[i] +=dp[i-j]
        return dp[-1]
                    
