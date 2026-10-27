class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i, j = 1, max(piles)
        res = j
        while i <= j:
            k = (i + j) // 2
            hr = 0

            for p in piles:
                hr += math.ceil(p / k)
            
            if hr <= h:
                res = min (res, k)
                j = k - 1
            else:
                i = k + 1

        return res
