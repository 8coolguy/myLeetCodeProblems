#lol that was easy got mines for the day real quick lol 50 on leet code
class Solution:
    def hammingWeight(self, n: int) -> int:
        count =0
        for i in range(32):
            if n >> i & 1:
                count+=1
        return count
