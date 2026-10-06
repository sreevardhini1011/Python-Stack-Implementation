class Stack:
    def __init__(self):
        self.data = []
        self.top = -1

    def put(self, value):
        self.data.append(value)
        self.top += 1

    def remove(self):
        if self.top == -1:
            raise IndexError("Stack is empty and there is nothing to pop out")

        value = self.data[self.top]
        self.data.pop()
        self.top -= 1
        return value

    def peek(self):
        if self.top == -1:
            raise IndexError("Stack is empty")

        return self.data[self.top]

    def is_empty(self):
        return self.top == -1
        return self.top == -1