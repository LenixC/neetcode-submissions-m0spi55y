class MinStack:

    def __init__(self):
        self.listy = []

    def push(self, val: int) -> None:
        self.listy.append(val)

    def pop(self) -> None:
        self.listy.pop()

    def top(self) -> int:
        return self.listy[len(self.listy) - 1]
        
    def getMin(self) -> int:
        return min(self.listy)
        
