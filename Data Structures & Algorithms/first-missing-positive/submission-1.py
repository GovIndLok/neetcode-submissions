class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        lowest_num = 1
        for i in range(len(nums)):
            if nums[i] == lowest_num and nums[i] > 0:
                lowest_num = lowest_num + 1

        return lowest_num