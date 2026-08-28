class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lent = len(numbers)
        ans = None
        i = 0
        j = lent - 1
        while not ans:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                ans = [min(i+1,j+1),max(i+1,j+1)]
        return ans