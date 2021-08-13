#I got this right,but it wasnt very effecient. For the the faster solution. I store the row and column into sets with fast entry times and iterate throuh that and set 0s not sure how that is faster but it significantly speeds up o nspace time.
#https://www.youtube.com/watch?v=mcyNRpopQeA gives good explanation 
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        flags =[[0 for _ in range(len(matrix[0]))] for i in range(len(matrix))]
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] ==0:
                    flags[i][j]=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if flags[i][j] ==1:
                    for x in range(len(matrix)):
                        matrix[x][j]=0
                    for y in range(len(matrix[i])):
                        matrix[i][y]=0
                    
                    
                        
                        
            

