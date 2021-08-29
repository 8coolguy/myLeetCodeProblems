class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        def dontOverlap(slot1,slot2):
            if startTime[slot1] >= endTime[slot2] or startTime[slot2] >=endTime[slot1]:
                return True
            return False 
        
        #I have to order the start times from largest to smallest to make this work
        print(startTime.sort())
        dp =profit.copy()
        n=len(profit)
        for i in range(n):
            #print(i)
            for j in range(i):
                #print(j)
                if dontOverlap(i,j):
                    dp[i] =max(dp[j]+profit[i],dp[i])
        #print(dp)
        return max(dp)
                
                
                
    
        
