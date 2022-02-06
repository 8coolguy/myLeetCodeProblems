#i think this solution works but not in the correct runtime
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==0:
            return True
        #my solution is that you start from the back and think of it from the back and if you can make it to the front 
        #have an array and store the result of your jumping into the array from last to front 
        
        dp=[False for _ in range(len(nums))]
        dp[-1]= True
        for i in range(len(nums)-2,-1,-1):
             
            for j in range(nums[i],-1,-1):
                if (j+i >=len(nums) or dp[j+i] ==True):
                    dp[i]=True
                    break
        return dp[0]
                
            
        
