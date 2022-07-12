class Solution:
    def numDecodings(self, s: str) -> int:
        #2 2 6
        # 2 /1
        # 2 2 /2
        # 2 2 6 /3
        
        #ex
        #142343
        
        #14 23 4 3
        #1 4 23 4 3
        #1 4 2 3 4 3
        #14 23 4 3
        #1 2 1 2 1 1 
        
        #ex
        # 112343 1 1 11 2 112 3 1123 5 11234 5 112343 5
        # 1 1 2 3 4 3
        # 11 2 3 4 3
        # 1 12 3 4 3
        #11 23 4 3  
        # 1 1 23 4 3
        
        #memoization
        dp = { len(s) : 1}
        
        def dfs(i):
            if i in dp:
                return dp[i]
            if int(s[i]) == 0:
                return 0 
            res =dfs(i+1)
            if i+1 < len(s) and int(s[i:i+2]) <= 26:
                res += dfs(i + 2)
            dp[i] = res
            return res
            
        return dfs(0)
        
            