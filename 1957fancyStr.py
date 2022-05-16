#first one that I did on the mac les goo chill problem
class Solution:
    def makeFancyString(self, s: str) -> str:
        l=[]
        res=""
        for i in range(len(s)):
            if i > 1 and s[i]==s[i-1] and s[i-2]==s[i]:
                continue
            res+=s[i]
        return res
        
