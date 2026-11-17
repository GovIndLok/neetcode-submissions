class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited_nodes = set()
        len_row = len(grid)
        len_col = len(grid[0])
        ans = 0

        def lands_visited(nx, ny):

            if nx > 0:
                if grid[nx - 1][ny] == "1" and (nx - 1, ny) not in visited_nodes:
                    visited_nodes.add((nx - 1, ny))
                    lands_visited(nx - 1, ny) 
            
            if ny > 0:
                if grid[nx][ny - 1] == "1" and (nx, ny - 1) not in visited_nodes:
                    visited_nodes.add((nx, ny - 1))
                    lands_visited(nx, ny - 1)

            if nx < len_row - 1:
                if grid[nx + 1][ny] == "1" and (nx + 1, ny) not in visited_nodes:
                    visited_nodes.add((nx + 1, ny))
                    lands_visited(nx + 1, ny)
                
            if ny < len_col - 1:
                if grid[nx][ny + 1] == "1" and (nx, ny + 1) not in visited_nodes:
                    visited_nodes.add((nx, ny + 1))
                    lands_visited(nx, ny + 1)

        for i in range(len_row):
            for j in range(len_col):
                if grid[i][j] == "1" and (i, j) not in visited_nodes:
                    visited_nodes.add((i,j))
                    lands_visited(i, j)
                    ans += 1

        return ans
