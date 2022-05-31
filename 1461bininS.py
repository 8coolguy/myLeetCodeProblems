#bruh i dk
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        return len(set(s[i:i+k] for i in range(len(s)-k+1))) == 2**k

        def its(k):
            res=[]
            getbinary = lambda x, n: format(x, 'b').zfill(n)
            for i in range(2**k):
                res.append(getbinary(i, k))
            return res
        for i in its(k):
            if not i in s:
                return False
        return True
                
