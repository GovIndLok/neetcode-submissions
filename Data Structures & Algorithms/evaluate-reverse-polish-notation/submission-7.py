class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        result = []
        for i in range(len(tokens)):
            match tokens[i]:
                case "+":
                    result.append(result.pop() + result.pop())
                case "-":
                    operands_one = result.pop()
                    operands_two = result.pop()
                    result.append(operands_two - operands_one)
                case "*":
                    result.append(result.pop() * result.pop())
                case "/":
                    operands_one = result.pop()
                    operands_two = result.pop()
                    result.append(int(operands_two / operands_one))
                case _:
                    result.append(int(tokens[i]))
        return result[0]