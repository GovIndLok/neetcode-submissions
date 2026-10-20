class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        len_num = len(nums)
        output = [1] * len_num

        for i in range(0, len_num):
            output[i] *= prefix
            output[len_num - 1 - i] *= postfix
            prefix *= nums[i]
            postfix *= nums[len_num - 1 - i]
        
        return output