#finally got this question which really just required a bunch of coding
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[{}]*9
        grids=[[{}]*3]*3
        cols=[{}]*9
        for r in range(9):
            for c in range(9):
                if board[r][c]!=".":
                    tmp=board[r][c]
                    print(f'{tmp}--{r//3}--{c//3}')
                    if tmp in grids[r//3][c//3]:
                        print("g")
                        print(grids)
                        return False
                    else:
                        
                        l=grids[r//3].copy()
                        my_dict=l[c//3].copy()
                        my_dict[tmp]="1"
                        l[c//3]= my_dict
                        grids[r//3]=l
                    if tmp in rows[r]:
                        print("r")
                        print(rows)
                        return False
                    else:
                        my_dict=rows[r].copy()
                        my_dict[tmp]="1"
                        rows[r]=my_dict
                    if tmp in cols[c]:
                        print("c")
                        print(cols)
                        return False
                    else:
                        my_dict=cols[c].copy()
                        my_dict[tmp]="1"
                        cols[c]=my_dict
        return True
                        