class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lnth = len(nums)

        for i in range(lnth):
            for j in range(i+1, lnth):
                if nums[i] + nums[j] == target:
                    return [i, j]