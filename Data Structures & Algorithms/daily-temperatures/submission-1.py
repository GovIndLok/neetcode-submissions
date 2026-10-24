class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, tmp in enumerate(temperatures):
            while stack and tmp > stack[-1][0]:
                stack_temp, stack_ind = stack.pop()
                result[stack_ind] = (i - stack_ind)
            stack.append([tmp, i])

        return result