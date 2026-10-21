class Solution:
    def trap(self, height: List[int]) -> int:
        size = len(height)
        if size == 0:
            return 0
        
        prefix = [0] * size
        suffix = [0] * size

        prefix[0] = height[0]
        for i in range(1, size):
            prefix[i] = max(prefix[i - 1], height[i])

        suffix[size - 1] = height[size - 1]
        for i in range(size - 2, -1, -1):
            suffix[i] = max(suffix[i + 1], height[i])

        water = 0
        for i in range(size):
            water += min(prefix[i], suffix[i]) - height[i]
        return water