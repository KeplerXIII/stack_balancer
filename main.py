class Stack:
    def __init__(self, stack=[]):
        self.stack = stack

    def __str__(self):
        return f'Наш стек: {self.stack}'

    def is_empty(self):
        if len(self.stack) == 0:
            return False
        else:
            return True

    def push(self, elem):
        self.stack.append(elem)

    def pop(self):
        if len(self.stack) == 0:
            return
        elem = self.stack[len(self.stack) - 1]
        del self.stack[len(self.stack) - 1]
        return elem

    def peek(self):
        return self.stack[len(self.stack) - 1]

    def size(self):
        return len(self.stack)




ex = Stack()
ex.push("a")
ex.push("b")
print(ex.pop())
print(ex)
print(ex.peek())
print(ex.size())
