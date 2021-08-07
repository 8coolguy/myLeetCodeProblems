#Yea  I dont get this one either so I looked it up. 
#I htink this explains it a bit https://www.tutorialcup.com/leetcode-solutions/stone-game.htm
#Dynamic Programing:
#I had to create a dp 2d array of 0s
#j-i %2 gives chance or smthg
#i dont actually understand whats gong on sooo.
#the other soulution i was closer to where if the sum of tiles even makes it then a player wins
#oh you can always win i had this thought but never subitted it wow
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return True
        def tot(arr):
            tot =0
            for i in arr:
                tot+=i
            return tot
        def takeGreatestEnd(piles):
            n =int(len(piles)/2)
            for i in range(n):
                if piles[0+i]>piles[-1-i]:
                    if(n>i+1 and piles[0+i+1] >piles[0+i] and piles[0+i+1]> piles[-1-1-i]):
                        return -1
                    return 0
                elif(piles[-1-i]>piles[0+i]):
                    if(n>i+1 and piles[-1-i-1]>piles[-1-i]>piles[0+i] and piles[-1-1-i]>piles[0+i+1]):
                        return 0
                    return -1
                else:
                    if(n>i+1 and piles[0+i+1] >piles[0+i]):
                        return -1
                    if(n>i+1 and piles[-1-i-1]>piles[-1-i]):
                        return 0
                
            #for i in range(n):
                
            return 0
        
        at=0
        st=0
        win =int(tot(piles)/2)
        for i in range(len(piles)):
            if i%2==0:
                print(at)
                at+=piles.pop(takeGreatestEnd(piles))
                if at>win:
                    return True
            else:
                print(st)
                st+=piles.pop(takeGreatestEnd(piles))
                if st>win:
                    return False
 
        
        if(at>st):
            return True
        else: False
        
        
        #real solution is just return True
