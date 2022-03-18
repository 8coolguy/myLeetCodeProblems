#ok solution i had a careless bug for so long anyway les get a nice streak for springbreak
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #quick solution
        my_dict={}
        for i in nums:
            if not my_dict.__contains__(i):
                my_dict[i]=True
        mc=0
        nums.sort()
        for i in nums:
            c=1
            j=i
            
            while(True):
                if my_dict.__contains__(j+1) and my_dict[j+1]:
                    c+=1
                    j+=1
                    my_dict[j]=False
                else:
                    break
                    
            if c>mc:
                mc=c
            #print(my_dict)
        return mc