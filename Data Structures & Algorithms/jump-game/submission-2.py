class Solution:
    def canJump(self, nums: List[int]) -> bool:
        len_nums = len(nums)

        reach = 0
        for i in range(len_nums):
            if i > reach:
                break
            reach = max(reach, nums[i] + i)

        return reach >= len_nums - 1