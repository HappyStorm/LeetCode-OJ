class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val_stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.min_stack += [min(x, self.min_stack[-1])] if self.min_stack else [x]
        self.val_stack += [x]

    def pop(self) -> None:
        self.min_stack.pop()
        self.val_stack.pop()

    def top(self) -> int:
        return self.val_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
