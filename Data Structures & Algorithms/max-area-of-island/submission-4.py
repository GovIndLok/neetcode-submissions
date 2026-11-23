class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area, curr_area = 0, 0
        len_row, len_col = len(grid), len(grid[0])
        def dfs(nx, ny):
            if nx < 0 or ny < 0 or nx > (len_row - 1) or ny > (len_col - 1) or grid[nx][ny] == 0:
                return 0

            grid[nx][ny] = 0
            return (1 + dfs(nx + 1, ny) + dfs(nx - 1, ny) + dfs(nx, ny + 1) + dfs(nx, ny - 1))
        
        for i in range(len_row):
            for j in range(len_col):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area