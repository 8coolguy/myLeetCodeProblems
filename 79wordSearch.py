#all my solution using back track 
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board ==None:
            return False

        visited=[]
        for i in range(len(board)):
            visited.append([])
            for _ in board[i]:
                visited[i].append(0)
        def BackTrack(m,n,i):
            visited[m][n]=1
            if (n >0):
                if(word[i]==board[m][n-1] and visited[m][n-1]!=1):
                    if i == len(word)-1 or BackTrack(m,n-1,i+1):
                        return True

            if(n < len(board[0])-1 and visited[m][n+1]!=1):
                if(word[i]==board[m][n+1]):
                    if i == len(word)-1 or BackTrack(m,n+1,i+1):
                        return True

            if (m >0):
                if(word[i]==board[m-1][n] and visited[m-1][n]!=1):
                    if i == len(word)-1 or BackTrack(m-1,n,i+1):
                        return True

            if(m < len(board)-1):
                if(word[i]==board[m+1][n] and visited[m+1][n]!=1):
                    if i == len(word)-1 or BackTrack(m+1,n,i+1):
                        return True
            visited[m][n]=0
            return False

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] ==word[0]:
                    if(len(word) ==1 or BackTrack(i,j,1) ):
                        return True

        return False




