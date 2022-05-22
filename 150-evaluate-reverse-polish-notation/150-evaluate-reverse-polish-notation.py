class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i.strip('-').isnumeric():
                stack.append(i)
            else:
                x, y = stack.pop(), stack.pop()
                stack.append(str(int(eval(y+i+x))))
        return stack[0]