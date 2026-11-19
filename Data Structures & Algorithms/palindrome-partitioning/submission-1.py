class Solution:
    def partition(self, s: str) -> List[List[str]]:
        len_s = len(s)
        ans = []
        part = []

        def dfs(i):
            if i >= len_s:
                ans.append(part.copy())
                return

            for j in range(i, len_s):
                if self.Pali(s, i, j):
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        
        dfs(0)
        return ans
    
    def Pali(self, string, left, right):
        while left < right:
            if string[left] != string[right]:
                return False
            
            left, right = left + 1, right - 1
        return True