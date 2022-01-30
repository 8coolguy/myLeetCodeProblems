#perfect nice
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        c =1
        pre=""
        if(len(strs)==1):
            return strs[-1]
        while True:
            for i in range(1,len(strs)):
                #print(strs[i])
                if(strs[i] ==""):
                    return ""
                if(strs[i][:c] !=strs[i-1][:c] or c > len(strs[i])):
                    return pre
            pre =strs[0][:c]
            c+=1
            
