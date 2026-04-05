# [
# [(
# [() 


left = '({['
right = ']})'

pairs = {']': '[', '}': '{', ')': '('}

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False

        stack = []

        for c in s:
            print(stack)
            print(c)
            if c in left:
                stack.append(c)
            elif c in right:
                if len(stack) < 1:
                    return False
                popped = stack.pop()
                print(f"{c}, {popped}")
                if pairs[c] != popped:
                    return False

        if len(stack) > 0:
            return False
        return True
        