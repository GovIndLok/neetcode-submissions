class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        ans = 0

        for n in numset:
            if n - 1 not in numset:
                lenth = 0
                while n + lenth in numset:
                    lenth += 1
                ans = max(ans, lenth)

        return ans