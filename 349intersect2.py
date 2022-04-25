#one of those super easy ones
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        my_dict = dict()
        for i in nums2:
            my_dict[i]=True
        res=dict()
        for i in nums1:
            if my_dict.__contains__(i):
                res[i]=0
        return list(res)
