#i guess i never did the fib
class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        res=[]
        res.append(0)
        res.append(1)
        for i in range(n-1):
            res.append(res[-1]+res[-2])
        return res[-1]
        