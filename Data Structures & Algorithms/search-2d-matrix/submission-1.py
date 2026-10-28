class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        if matrix[0][0] == target or matrix[m-1][n-1] == target:
            return True

        i = 0
        j = (m*n) - 1

        while i <= j:
            curr = (i+j) // 2

            curr_i = curr // n 
            curr_j = curr % n

            if matrix[curr_i][curr_j] < target:
                i = curr + 1
            elif matrix[curr_i][curr_j] > target:
                j = curr - 1
            else:
                return True
        
        return False