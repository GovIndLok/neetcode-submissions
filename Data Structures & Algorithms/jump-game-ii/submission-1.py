class Solution:
    def jump(self, nums: List[int]) -> int:
        len_nums = len(nums)

        left, right = 0, 0
        count = 0
        while left < len_nums - 1 and right < len_nums - 1:
            farest = 0
            for i in range(left, right + 1):
                farest = max(farest, nums[i] + i)
            count += 1

            left = right + 1
            right = farest 
        
        return count