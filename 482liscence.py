class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        cur=0
        res=[]
        for i in s[::-1]:
            if i =="-":
                continue
            if cur==k:
                res.append('-')
                cur=0
                
            cur+=1
            res.append(i.upper())
        return "".join(res)[::-1]
        
        