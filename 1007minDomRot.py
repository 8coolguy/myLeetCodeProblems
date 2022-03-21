#finished this problem you have to calculate the min steps
class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        top_count={}
        bot_count={}
        same=0
        for i in range(7):
            top_count[i+1]=0
            bot_count[i+1]=0
        for i in range(len(tops)):
            top_count[tops[i]]+=1
            bot_count[bottoms[i]]+=1
            if bottoms[i] ==tops[i]:
                same+=1
        for i in range(7):
            if top_count[i+1] +bot_count[i+1]- same ==len(tops):
                return len(tops)-max(top_count[i+1], bot_count[i+1])
        return -1
            
        
        