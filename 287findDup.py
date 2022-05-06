class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo=0
        hi=len(nums)-1
        #binary search method
        while hi >= lo:
            mi =(lo+hi)//2
            c=0
            #tries to count the number of eles that are greater than that one
            for i in nums:
                if mi >= i:
                    c+=1
            if (c <= mi): 
                lo = mi + 1;
            else:
                hi = mi - 1;
        return lo
        