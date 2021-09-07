class Solution:
    def reverse(self, x: int) -> int:
        y=int()
        if int(x) <0:
            x =str(int(x)*-1)
            print("".join([list(str(x))[-1*(i+1)] for i in range(len(str(x)))]))
            y=-1 *int("".join([list(str(x))[-1*(i+1)] for i in range(len(str(x)))]))
        else: 
            y=int("".join([list(str(x))[-1*(i+1)] for i in range(len(str(x)))]))
        if y>2**31-1 or y<-2**31: 
            return 0
        else: return y
        
