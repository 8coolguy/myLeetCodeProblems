class Solution:
    def climbStairs(self, n: int) -> int:
        #3 
        #recursive
        #result =0
        #if(n==1 or n==0):
           # result+=1
        #else:
            #result=self.climbStairs(n-1) + self.climbStairs(n-2)
        #return result
        #memoization of recursive 
        #def fib(n,memo):
         #   if(memo[n]!=None):
         #       return memo[n]
        #    result=0
         #   if(n==1 or n==0):
       #         result+=1
       #         memo[n]=1
         #   else:
        #        result=fib(n-1,memo) +fib(n-2,memo)
        #        memo[n]=result
        #    return result
       # memo_arr =[None]*(n+1)
        #return fib(n, memo_arr)
        
        #bottom up
        memo_arr=[None] *(n+1)
        memo_arr[0]=1
        memo_arr[1]=1
        
        for i in range(2,n+1):
            memo_arr[i]=memo_arr[i-1]+memo_arr[i-2]
        return memo_arr[n]
        
        
        
        #n1 1
        #n2 2
        #n3 3
        #n4 5
        #n5 11111 221 122 212 1112 2111 1211 1121 8