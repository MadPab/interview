# TASK 1

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")  

    def size(self):
        return len(self.items)


stack = Stack()

print(stack.is_empty())
stack.push('This')
stack.push('is')
stack.push('Python')
print(stack.items[0], stack.items[1], stack.items[2])
print(stack.size())
print(stack.peek())
print(stack.pop())
print(stack.size())
print(stack.is_empty())


# TASK 2


def is_balanced(brackets):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}

    for bracket in brackets:
        if bracket in "({[":
            stack.push(bracket)
        elif bracket in ")}]":

            if stack.is_empty() or stack.pop() != pairs[bracket]:
                return "Несбалансированно"    

    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"


print(is_balanced("(((([{}]))))"))
print(is_balanced("[([])((([[[]]])))]{()}"))
print(is_balanced("{{[()]}}"))
print(is_balanced("}{"))
print(is_balanced("{{[(])]}"))
print(is_balanced("[[{())}]"))
