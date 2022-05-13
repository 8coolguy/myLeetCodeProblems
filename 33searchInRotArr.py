#not easy but very intutive and I get completely could teach to kindergardener
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo =0
        hi =len(nums)-1
        # return the index of target or negative one if not exists
        while hi >= lo:
            
            mi = (hi+lo)//2
            print(mi)
            if nums[mi] ==target:
                return mi
            if nums[lo] <=nums[mi]:#the start is on the right side
                if nums[mi]>= target >= nums[lo]:
                    hi=mi-1
                else:
                    lo=mi+1
            else:#the start is on the left side
                if nums[mi]<= target <=nums[hi]:
                    lo=mi+1
                else:
                    hi=mi-1
                
                
                
        return -1
