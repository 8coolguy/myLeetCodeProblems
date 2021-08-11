#you need to use some tree  map thing ill review the problems of this week on sunday cause this was hard#my algo passed 70 of the tests
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        def find(ele,ele2,arr,i,flags,flags2):
            ans =False
            for j in range(len(arr)):
                if j!=i and (ele ==arr[j] or ele2 ==arr[j]) and (flags[j]==0 or flags2[j]==0):
                    if ele ==arr[j]:
                        flags[j]=1
                    else:flags2[j]=1
                    ans= True
            print(ans)
            return ans
        flags =[0 for _ in range(len(arr))]
        flags2 =[0 for _ in range(len(arr))]
        for i in range(int(len(arr))):
            j=2*arr[i] 
            k =int(arr[i]/2)
            if not find(j,k,arr,i,flags,flags2):
                return False
            print(flags)
        return True
        
    
        
        
