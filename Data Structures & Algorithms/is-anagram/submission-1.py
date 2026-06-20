class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_char = collections.Counter(s)
        for i in t:
            if s_char.get(i, 0) <= 0:
                return False
            s_char[i] -= 1
        return True