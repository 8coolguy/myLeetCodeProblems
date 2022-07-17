class Solution:
    def isHappy(self, n: int) -> bool:
        #it sucks dude but i got it first submit after one mistake
        my_dict={}
        def next(n):
            if n in my_dict:
                return False
            else:
                my_dict[n]=1
            tot=0
            while n !=0:
                tot+=(n%10)**2
                n=n//10
            print(tot)
            if tot==1:
                return True
            else:
                return next(tot)
        return next(n)
        