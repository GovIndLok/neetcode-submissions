class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area, curr_area = 0, 0
        visited_node = set()
        len_row, len_col = len(grid), len(grid[0])
        def dfs(nx, ny):
            if nx < 0 or ny < 0 or nx > (len_row - 1) or ny > (len_col - 1) or (nx, ny) in visited_node:
                return 0
            visited_node.add((nx, ny))
            if grid[nx][ny] == 1:
                return (1 + dfs(nx + 1, ny) + dfs(nx - 1, ny) + dfs(nx, ny + 1) + dfs(nx, ny - 1))
            else:
                return 0
        
        for i in range(len_row):
            for j in range(len_col):
                if grid[i][j] == 1 and (i, j) not in visited_node:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area