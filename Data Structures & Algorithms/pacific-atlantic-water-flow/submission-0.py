class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        len_row = len(heights)
        len_col = len(heights[0])
        pecific = set()
        atlantic = set()

        
        def dfs(nx, ny, ocean, prevNode):

            if ((nx, ny) in ocean or nx < 0 or ny < 0 or nx == len_row or ny == len_col) or heights[nx][ny] < prevNode:
                return
            
            ocean.add((nx, ny))
            dfs(nx - 1, ny, ocean, heights[nx][ny])
            dfs(nx + 1, ny, ocean, heights[nx][ny])
            dfs(nx, ny - 1, ocean, heights[nx][ny])
            dfs(nx, ny + 1, ocean, heights[nx][ny])
        
        for row in range(len_row):
            dfs(row, 0, pecific, heights[row][0])
            dfs(row, len_col - 1, atlantic, heights[row][len_col - 1])

        for col in range(len_col):
            dfs(0, col, pecific, heights[0][col])
            dfs(len_row - 1, col, atlantic, heights[len_row - 1][col])

        
        ans = []
        for row in range(len_row):
            for col in range(len_col):
                if (row, col) in pecific and (row, col) in atlantic:
                    ans.append([row, col])

        return ans