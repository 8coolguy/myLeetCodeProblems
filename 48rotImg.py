#jsut had to store in array and do some array math
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        temp=[]
        for i in matrix:
            for j in i:
                temp.append(j)
        print(temp)
        for i in range(len(matrix)):
            for j in range(len(matrix )):
                matrix[i][j]=temp[-(len(matrix)*(j+1)-i)]
        print(matrix)
