#i still barely understood alot of how bit shifting works in this context so I need to do more pactice
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff

        # in Python, every integer is associated with its two's complement and its sign.
        # However, doing bit operation "& mask" loses the track of sign. 
        # Therefore, after the while loop, a is the two's complement of the final result as a 32-bit unsigned integer. 
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
            print(b)
            print(a)

        # a is negative if the first bit is 1
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a
            
