class Stack:
    def __init__(self):
        self.stack = []
        self.len = len(self.stack)
    def isEmpty(self):
        if self.stack == []:
            return True
        else:
            return False
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[self.len-1]
    def bottom(self):
        return self.stack[0]

