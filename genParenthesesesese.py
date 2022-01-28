#ayy thats how you do dp
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # we need to use dp 
        # go from n to  0
        # 1 "()"
        # 2 i=1+0 "(())"  i = 1+ 1 ()()"
        # 3 i=1+0 (()()) i =1+1 ((())) i =1+2 (()()) j=1 i=0+1 (())
       
            
            
        dp = [[] for _ in range(n+1)]
        dp[1].append("()")
        if(n ==0 or n==1):
            return dp[n]
        #print(dp[1])
        for k in range(2,n+1):
            my_set =set()
            
            for j in range(len(dp[k-1])):
                for i in range(n):
                    #print(dp[k-1][j][:i+1]+"()"+dp[k-1][j][i+1:])
                    my_set.add(dp[k-1][j][:i+1]+"()"+dp[k-1][j][i+1:])
            dp[k]=list(my_set)
        return dp[-1]
                    
            #  to go from 0 to number you want
            
