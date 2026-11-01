class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        i_map = set()

        l = 0
        ans = 0
        
        for r in range(len(s)):
            while s[r] in i_map:
                i_map.remove(s[l])
                l = l + 1

            i_map.add(s[r])
            
            ans = max(ans, (r - l + 1))
        
        return ans