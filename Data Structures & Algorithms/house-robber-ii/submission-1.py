class Solution:
    def rob(self, nums: List[int]) -> int:
        len_nums = len(nums)
        if len_nums < 3:
            return max(nums[0], nums[-1])

        ans1, ans2 = 0, 0
        final_ans = []
        for i in range(1, len_nums):
            tmp = max(nums[i] + ans1, ans2)
            ans1 = ans2
            ans2 = tmp
        final_ans.append(ans2)
        ans1, ans2 = 0, 0
        for i in range(0, len_nums - 1):
            tmp = max(nums[i] + ans1, ans2)
            ans1 = ans2
            ans2 = tmp
        final_ans.append(ans2)
        
        return max(final_ans)