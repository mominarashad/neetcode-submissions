class Solution:
    def isValid(self, s: str) -> bool:

        stack=[]

        map={')':'(','}':'{',']':'['}

        for ch in s:

            if ch in map.values():
                stack.append(ch)
            else:
                if not stack or map[ch]!=stack[-1]:
                     return False
                stack.pop()


        return not stack
        