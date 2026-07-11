class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(ch.lower() for ch in s if ch.isalnum()) 
        len_s = len(s)
        left = 0
        right = len_s - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True