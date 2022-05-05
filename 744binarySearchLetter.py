#bro what I couldnt even do a binary search also 100 problems
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        lo=0
        hi=len(letters)-1
        m=0
        while hi >= lo:
            m=(hi+lo)//2
            if letters[m] <= target:
                lo=m+1
            if target < letters[m]:
                hi = m-1
         
        return letters[lo]
        