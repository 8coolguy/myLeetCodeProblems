#my algo works after alot of random bugs
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #first row 0 then col -1 then row -1 then col 0
        res=[]
        while matrix !=[]:
            
            for i in matrix[0]:
                res.append(i)
            matrix.pop(0)
            if matrix ==[]:
                break
            rem=[]
            for i in range(len(matrix)):
                if matrix[i]!=[]:
                    res.append(matrix[i][-1])
                    matrix[i].pop()
                
            print(matrix)      
            if matrix ==[]:
                break
            for i in range(len(matrix[-1])-1,-1,-1):
                res.append(matrix[-1][i])
            matrix.pop()
            print(matrix)
            if matrix ==[]:
                break
            print(len(matrix))
            for i in range(len(matrix)-1,-1,-1):
                if matrix[i]!=[]:
                    print(matrix[i])
                    print(matrix)
                    res.append(matrix[i][0])
                    matrix[i].pop(0) 
                
            print(matrix)    
            if matrix ==[]:
                break
        return res
            
        
        
