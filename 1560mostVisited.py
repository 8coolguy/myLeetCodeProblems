#gonna go crazy on this new streak 2
#not sure what the runtime is probably need to revisit this
class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        self.n=n
        mydict={}
        for i in range(n):
            mydict[i+1]=0

        start=rounds[0]
        for i in range(1,len(rounds)):
            while(start!=rounds[i]):
                mydict[start]+=1
                start=self.next_index(start,n)
        mydict[start]+=1
        print(mydict)
        mycount = max(list(mydict.values()))
        res=[]
        for i in list(mydict):
            if mydict[i] ==mycount:
                res.append(i)
        return res
