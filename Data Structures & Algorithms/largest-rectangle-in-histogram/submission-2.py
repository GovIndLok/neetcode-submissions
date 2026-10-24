class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_hieght = 0
        for i, h in enumerate(heights):
            start_index = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_hieght = max(max_hieght, height * (i - index))
                start_index = index
            stack.append([start_index, h])

        for i, h in stack:
            max_hieght = max(max_hieght, h * (len(heights) - i))

        return max_hieght