class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        stack = []
        for char in s:
            print(char)
            if char == ']':
                if not stack:
                    return False
                popped = stack.pop()
                if popped != '[':
                    return False
            elif char == '}':
                if not stack:
                    return False
                popped = stack.pop()
                if popped != '{':
                    return False
            elif char == ')':
                if not stack:
                    return False
                popped = stack.pop()
                if popped != '(':
                    return False
            else:
                stack.append(char)
                print(stack)
        
        if stack:
            return False
        return True