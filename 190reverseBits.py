#not my solution but i can understand it complelelty 
#line 7 moves last bit in to out and the next line moves the bit over or smthng 
#need to learn bit manipilation in python
class Solution:
    def reverseBits(self, n):
        out = 0
        for i in range(32):
            out = (out << 1)^(n & 1)
            n >>= 1
        return out

