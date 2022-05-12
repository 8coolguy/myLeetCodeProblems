#super trash solution on the day but got some done
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=[]
        sets=[]
        for i in strs:
            my_set=list(i)
            my_set.sort()
            b=True
            for j in range(len(sets)):
                if my_set ==sets[j]:
                    res[j].append(i)
                    b=False
            if b:
                sets.append(my_set)
                res.append([i])
        return res
                    
            