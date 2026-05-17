class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opt = {"+", "-", "*", "/"}
        for t in tokens:
            if t not in opt:
                stack.append(int(t))
            else:
                second = stack.pop()
                first = stack.pop()
                
                if t == "+":
                    stack.append(first + second)
                elif t == "-":
                    stack.append(first - second)
                elif t == "*":
                    stack.append(first * second)
                elif t == "/":
                    stack.append(int(first / second))
        return stack[0] 

