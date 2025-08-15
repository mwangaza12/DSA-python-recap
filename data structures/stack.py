class Stack:
    def __init__(self):
        self._data = []

    def push(self, x):
        """Add an element to the top of the stack."""
        self._data.append(x)

    def pop(self):
        """Remove and return the top element of the stack."""
        if not self._data:
            raise IndexError("pop from empty stack")
        return self._data.pop()

    def peek(self):
        """Return the top element without removing it."""
        if not self._data:
            raise IndexError("peek from empty stack")
        return self._data[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return not self._data

    def size(self):
        """Return the number of elements in the stack."""
        return len(self._data)


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top element:", stack.peek())     # 30
    print("Stack size:", stack.size())      # 3
    print("Popped:", stack.pop())           # 30
    print("Popped:", stack.pop())           # 20
    print("Is empty?", stack.is_empty())    # False
    print("Popped:", stack.pop())           # 10
    print("Is empty?", stack.is_empty())    # True
