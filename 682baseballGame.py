#easy there might be a way to make the memory constant
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        if not ops:
            return 0
        res=[]
        #last_one=0
        #second_last=0
        #total=0
        for c in ops:   
            if "C" == c:
                res.pop()
            elif "D" ==c:
                res.append(int(res[-1]*2))
            elif "+" ==c:
                res.append(int(res[-1]+res[-2]))
            else:
                res.append(int(c))
        return sum(res)
        