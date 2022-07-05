class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        c=numBottles
        empty=0
        while numBottles>=numExchange:
            c+=(numBottles)//numExchange
            numBottles-=(numBottles//numExchange)*(numExchange-1)
            # N-=(N//E)*(E-1)
        return c
            
        