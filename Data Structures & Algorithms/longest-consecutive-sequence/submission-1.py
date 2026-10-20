class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numss = set(nums)
        ans = 0

        for n in numss:
            if n - 1 not in numss:
                lenth = 0
                while n + lenth in numss:
                    lenth += 1
                ans = max(ans, lenth)

        return ans