#my complexity is too slow need to check on this on sunday

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def isAnagram(ele,ana):
            used =[]
            x=len(ana)
            for s in ele:
                y=True
                for a in range(x):
                    if s ==ana[a] and used.count(a)==0:
                        used.append(a)
                        y=False
                        break
                if(y):
                    return False
                        
            if len(used)==x and len(ele)==x:
                return True
            return False
        ans=[]
        c=0
        
        for i in range(len(strs)):
            if len(strs)==0:
                break
            ans.append([])
            temp=strs.pop(0)
            ans[c].append(str(temp))
            popped=0`
            for j in range(len(strs)):
                temp1=str(strs[j-popped])
                if isAnagram(temp,temp1):
                    ans[c].append(strs.pop(j-popped))
                    popped+=1
            c+=1
        
        return ans            

