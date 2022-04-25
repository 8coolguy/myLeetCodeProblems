#wow look at that sexy optimization went from o(n^3) to O(n^4) to alittle faster in O(n^2) i think
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        res=0
        #my_dict={}
        #for i in nums4:
        #    if my_dict.__contains__(i):
        #        my_dict[i]+=1
        #    else:
        #        my_dict[i]=1
        #for i in nums1:
        #    for j in nums2:
        #        for k in nums3:
        #            if my_dict.__contains__(-1*(i+j+k)):
        #                res+=my_dict[-1*(i+j+k)]
        arr1=[]
        arr2=[]
        for i in nums1:
            for j in nums2:
                arr1.append(i+j)
        for i in nums3:
            for j in nums4:
                arr2.append(i+j)
        my_dict={}        
        for i in arr2:
            if my_dict.__contains__(i):
                my_dict[i]+=1
            else:
                my_dict[i]=1
        for i in arr1:
            #for j in arr2:
            #    if i+j ==0:
            #        res+=1
            if my_dict.__contains__(i*-1):
                res+=my_dict[-1*i]
            
                
            
            
            
        
        return res
                        
                    
                    
        
