class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lft, rit = 0, len(nums)-1

        while lft <= rit:
            m = (lft+rit) // 2
            if nums[m] > target:
                rit = m - 1
            elif nums[m] < target:
                lft = m + 1
            else:
                return m
        
        return -1