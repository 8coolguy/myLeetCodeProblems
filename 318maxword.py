#some rray problems
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        arr=[]
        ls=[]
        for i in words:
            arr.append(set(i))
            ls.append(len(i))
        m=0
        for i in range(len(ls)):
            for j in range(i+1,len(ls)):
                if ls[i]*ls[j]>m:
                    cond=True
                    for k in arr[i]:
                            if k in arr[j]:
                                cond=False
                    if cond:
                        m=ls[i]*ls[j]
        return m
                        
        