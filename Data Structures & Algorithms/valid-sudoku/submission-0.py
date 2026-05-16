class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        
        for i in range(9):
            row = []
            col = []
            for j in range(9):
                if board[i][j] != ".":
                    row.append(board[i][j])
                    
                if board[j][i] != ".":
                    col.append(board[j][i])
                    

            for x in Counter(row).values():
                if x>1:
                    return False
            
            for x in Counter(col).values():
                if x>1:
                    return False
        
        for i in [0,3,6]:
            for j in [0,3,6]:
                grid = [
                    board[i][j], board[i][j+1], board[i][j+2],
                    board[i+1][j], board[i+1][j+1], board[i+1][j+2],
                    board[i+2][j], board[i+2][j+1], board[i+2][j+2]
                ]

                grid = [x for x in grid if x != '.']
                
                for x in Counter(grid).values():
                    if x>1:
                        return False
                
        return True     