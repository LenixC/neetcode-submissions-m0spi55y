class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == '+':
                n1 = stack.pop()
                n2 = stack.pop()
                
                stack += [n2, n1, n1+n2]
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                n1 = stack.pop()
                stack += [n1, n1*2]
            else:
                stack.append(int(op))
            print(stack)
        
        return sum(stack)