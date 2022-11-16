# объявляем класс

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

# создаём балансер

def balancer(data: str) -> str:
    bracket_list = list(data)
    stack = Stack(stack=data)
    stack_len = stack.size()
    first_half = "".join(bracket_list[0:int(stack_len / 2)])
    second_half = "".join(bracket_list[int(stack_len / 2):])
    first_half = first_half.replace('[', ']').replace('{', '}').replace('(', ')')
    if second_half == first_half[::-1]:
        return "Сбалансировано"
    else:
        return "Несбалансированно"


if __name__ == '__main__':
    pass
