class Solution:
    def convert(self, s: str, numRows: int) -> str: 
        #123212321232123122312231231231231231231231
        if len(s) <2 or numRows <2:
            return s
        
        up=True
        i=0
        res=['']*numRows
        for c in s:
            #print(c)
            #print(i)
            res[i]+=c
            if up:
                i+=1
            else:
                i-=1
            if i==numRows-1 or i==0:
                up = not up
        res="".join(res)
        return res
            
