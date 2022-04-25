# ishould redo with more time
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #given an array i need to make the number some how
        res=0
        for i in range(len(digits)):
            res+=digits[-1-i]*10**i
            
        res+=1
        return list(str(res))
            
    