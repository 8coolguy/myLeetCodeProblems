#did not finsih yet will comeback tommorow 
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        
        top_count={}
        bot_count={}
        for i in tops:
            if top_count.__contains__(i):
                top_count[i]+=1
            else:
                top_count[i]=1
        for j in bottoms:
            if bot_count.__contains__(j):
                bot_count[j]+=1
            else:
                bot_count[j]=1
        print(top_count)
        print(bot_count)
            
        