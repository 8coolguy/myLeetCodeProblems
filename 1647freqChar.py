class Solution:
    def minDeletions(self, s: str) -> int:
        a=[""]*(len(s)+1)
        d=dict()
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d.keys():
            a[d[i]]+=i
        c=0
        for i in range(len(a)-1,0,-1):
            if len(a[i])>1:
                c+=len(a[i])-1
                a[i-1]+="_"*(len(a[i])-1)
        return c
                