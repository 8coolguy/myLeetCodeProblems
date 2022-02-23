#kinda got luck I noticed the pattern STREAK 1
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res=0
        l=len(columnTitle)
        for i in columnTitle:
            l-=1
            res+= 26**l * (ord(i)-64)
            print(res)
        return res
