class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        present = {}
        lowest_num = 1

        for i in range(len(nums)):
            curr_num = nums[i]
            if curr_num == lowest_num:
                present[curr_num] = True
                k = 1
                while lowest_num + k in present:
                    k = k + 1
                lowest_num += k
            if curr_num not in  present:
                present[curr_num] = True

        return lowest_num