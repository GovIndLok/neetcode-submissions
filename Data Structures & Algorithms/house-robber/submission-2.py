class Solution:
    def rob(self, nums: List[int]) -> int:
        ans1, ans2 = 0,0
        len_nums = len(nums)
        for i in nums:
            temp = max(i + ans1, ans2)
            ans1 = ans2
            ans2 = temp
        
        return ans2
