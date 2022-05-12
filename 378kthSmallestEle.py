#first solution was mine this solution was created by reading someone elses and following the logic
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        lo=matrix[0][0]
        hi=matrix[-1][-1]
        n=len(matrix)
        def countLessOrEqual(x):
            cnt = 0
            c = n - 1  # start with the rightmost column
            for r in range(n):
                while c >= 0 and matrix[r][c] > x: c -= 1  # decrease column until matrix[r][c] <= x
                cnt += (c + 1)
            return cnt
        
        res=0
        while hi>=lo:
            mi=(hi+lo)//2
            if countLessOrEqual(mi) >= k:
                res=mi
                hi=mi-1
            else:
                lo=mi+1
        return res
