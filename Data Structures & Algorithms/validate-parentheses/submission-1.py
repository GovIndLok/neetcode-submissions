class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brakets = {')':'(','}':'{',']':'['}
        
        for braket in s:
            if braket in brakets:
                if stack and stack[-1] == brakets[braket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(braket)

        
        if not stack:
            return True
        else:
            return False