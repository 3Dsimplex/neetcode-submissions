class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for let in s:
            print(stack)
            if let == '(' or let == '[' or let == '{':
                stack.append(let)
                continue
            if let == ')':
                if (not stack): return False
                init = stack.pop()
                if init == '(': continue
                else: return False
            if let == ']':
                if (not stack): return False
                init = stack.pop()
                if init == '[': continue
                else: return False
            if let == '}':
                if (not stack): return False
                init = stack.pop()
                if init == '{': continue
                else: return False
            return False
        if stack: return False
        return True