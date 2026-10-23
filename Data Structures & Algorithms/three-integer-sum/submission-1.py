class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        total_nums = len(nums)
        nums.sort()
        for i in range(total_nums-2):
            
            j = i+1
            k = total_nums - 1
            target = -(nums[i])
            while j < k:
                if nums[j] + nums[k] < target:
                    j += 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    if [nums[i], nums[j], nums[k]] not in output:
                        output.append([nums[i], nums[j], nums[k]])
                    k -= 1
        
        return output