class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        len_word = len(word)
        len_row = len(board)
        len_col = len(board[0])
        hash = set()

        def backtrack(wi, bx, by):
            if wi == len_word:
                return True
            
            if bx > 0:
                if board[bx - 1][by] == word[wi] and (bx - 1, by) not in hash:
                    hash.add((bx - 1, by))
                    if backtrack(wi + 1, bx - 1, by):
                        return True
                    else:
                        hash.remove((bx - 1, by))
                
            
            if by > 0:
                if board[bx][by - 1] == word[wi] and (bx, by - 1) not in hash:
                    hash.add((bx, by - 1))
                    if backtrack(wi + 1, bx, by - 1):
                        return True
                    else:
                        hash.remove((bx, by - 1))

            if bx < (len_row - 1):
                if board[bx + 1][by] == word[wi] and (bx + 1, by) not in hash:
                    hash.add((bx + 1, by))
                    if backtrack(wi + 1, bx + 1, by):
                        return True
                    else:
                        hash.remove((bx + 1, by))
            
            if by < (len_col - 1):
                if board[bx][by + 1] == word[wi] and (bx, by + 1) not in hash:
                    hash.add((bx, by + 1))
                    if backtrack(wi + 1, bx, by + 1):
                        return True
                    else:
                        hash.remove((bx, by + 1))

            return False
        
        for i in range(len_row):
            for j in range(len_col):
                if board[i][j] == word[0]:
                    hash.add((i,j))
                    if backtrack(1, i, j):
                        return True
                    hash.remove((i,j))
        
        return False