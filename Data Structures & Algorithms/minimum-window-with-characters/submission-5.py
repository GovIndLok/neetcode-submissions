class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = {}
        windows = {}

        for c in t:
            if c in countT:
                countT[c] += 1
            else:
                countT[c] = 1

        h, n = 0, len(countT)
        res, resl = [-1,-1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in windows:
                windows[c] += 1
            else:
                windows[c] = 1

            if c in countT and windows[c] == countT[c]:
                h += 1
            
            while h == n:
                if (r - l + 1) < resl:
                    res = [l,r]
                    resl = (r - l + 1)

                windows[s[l]] -= 1
                if s[l] in countT and windows[s[l]] < countT[s[l]]:
                    h -= 1
                
                l += 1

        l, r = res

        return s[l:r+1] if resl != float("infinity") else ""