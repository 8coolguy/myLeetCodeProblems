#on my own a bit slow but gets it done
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        #perm=[]


        def dfs(k,perm):
            res.append(perm[:])
            print(res)
            for n in range(k,len(nums)):
                perm.append(nums[n])
                print(perm)
                dfs(n+1,perm)
                perm.pop()
        dfs(0,[])
        return res

