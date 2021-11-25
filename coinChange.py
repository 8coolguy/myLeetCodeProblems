class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #different amount of coins and amount for the total amt of  
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            for coin in coins:
                if i-coin >= 0:
                    dp[i] =min(dp[i],dp[i-coin]+1)
        print(dp)
        if(dp[-1]==float('inf')):
            return -1
        else:
            return dp[-1]
        
        ##Recursive soultion 
#not mine solution