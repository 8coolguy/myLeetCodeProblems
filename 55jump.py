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
                
class Solution22:
    def canJump(self, nums: List[int]) -> bool:
        #rewrote the solution in O(n) insteasd of previos of O(n^2)
        #sets max reached
        max_index=0
        for i in range(len(nums)):
            #if iterate past max reached it failed
            if i > max_index:
                return False
            #get the new max_reached from amt jump base
            max_index = max(max_index, i+nums[i])
        return True    
        
