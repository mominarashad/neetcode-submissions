class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for ch in operations:
            if ch.lstrip('-').isdigit():
                stack.append(int(ch))
            elif ch == '+':
                a = stack[-1]
                b = stack[-2]
                stack.append(a + b)
            elif ch == 'C':
                stack.pop()
            else:  # 'D'
                stack.append(2 * stack[-1])

        return sum(stack)