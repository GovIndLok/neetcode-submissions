class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        appear = {}
        for i in nums:
            if i not in appear:
                appear[i] = True
            elif i in appear:
                return appear[i]
        
        return False