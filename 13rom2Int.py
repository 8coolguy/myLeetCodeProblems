#clutch win les go ez just think big brain
class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        tot=0
        for i in range(len(s)-1,-1,-1):
            if i==len(s)-1:
                tot+=d[s[i]]
            else:
                if d[s[i]] >= d[s[i+1]]:
                    tot+=d[s[i]]
                else:
                    tot-=d[s[i]]
        return tot
            
            
        
