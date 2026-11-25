class trie:
    def __init__(self) -> None:
        self.val = dict()
        self.EndWord = None
        self.index = -1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        wordTree = trie()
        
        for word_ind in range(len(words)):
            currNode = wordTree
            
            for char in words[word_ind]:
                if char not in currNode.val:
                    currNode.val[char] = trie()
                
                currNode = currNode.val[char]
            
            currNode.EndWord = True
            currNode.index = word_ind
        
        ans = []
        len_row = len(board)
        len_col = len(board[0])
        def dfs(nx, ny, currNode):
            if currNode.EndWord and currNode.index != -1:
                ans.append(words[currNode.index])
                currNode.index = -1

            if nx < 0 or ny < 0 or nx >= len_row or ny >= len_col or board[nx][ny] not in currNode.val or board[nx][ny] == '#':
                return 
            
            curr = currNode.val[board[nx][ny]]
            temp = board[nx][ny]
            board[nx][ny] = '#'
            dfs(nx - 1, ny, curr)
            dfs(nx + 1, ny, curr)
            dfs(nx, ny - 1, curr)
            dfs(nx, ny + 1, curr)
            board[nx][ny] = temp

        for i in range(len_row):
            for j in range(len_col):
                if board[i][j] in wordTree.val:
                    dfs(i, j, wordTree)
        
        return ans