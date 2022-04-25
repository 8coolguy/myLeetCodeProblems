#leared a function called counter now very simple solution that may have been hard to implement
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c =collections.Counter(nums1)
        
        res=[]
        
        for num in nums2:
            if c[num] > 0:
                res.append(num)
                c[num]-=1
        return res
