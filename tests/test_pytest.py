from main import Stack, balancer
import pytest

# тестируем методы созданного класса, скелет без FIXTURE массива переменных

def test_is_empty():
    stack = Stack()
    result = stack.is_empty()
    assert result == False
    stack_1 = Stack(stack=[1, 2, 3])
    result = stack_1.is_empty()
    assert result == True


def test_push_pop():
    stack = Stack(stack=["a", "b", "c"])
    stack.push('d')
    result = stack.pop()
    assert result == 'd'


def test_peek():
    stack = Stack(stack=["a", "b", "c"])
    result = stack.peek()
    assert result == "c"


def test_size():
    stack = Stack(stack=["a", "b", "c"])
    result = stack.size()
    assert result == 3


# Тестируем балансировщик

FIXTURE = [
    ('(((([{}]))))', 'Сбалансировано'),
    ('{{[()]}}', 'Сбалансировано'),
    ('}{}', 'Несбалансированно'),
    ('{{[(])]}}', 'Несбалансированно'),
    ('[[{())}]', 'Несбалансированно')
]

@pytest.mark.parametrize("data, etalon", FIXTURE)
def test_balancer(data, etalon):
    result = balancer(data)
    assert result == etalon