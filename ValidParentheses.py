class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {")" : "(", "]" : "[", "}" : "{"}
        stack = []
        for char in s:
            if char not in close_to_open:
                stack.append(char)
                continue
            if not stack or stack[-1] != close_to_open[char]:
                return False
            else:
                stack.pop()
        return not stack
